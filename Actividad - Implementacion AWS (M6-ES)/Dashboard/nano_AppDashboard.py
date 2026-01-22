import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from pyathena import connect

# =========================
# Configuración Athena
# =========================
REGION = "us-east-1"
S3_STAGING_DIR = "s3://bucket-data-mastodon/athena/"
DATABASE = "MastodonAnalysis"
TABLE = "mastodon_sentiment"

# =========================
# Utilidades
# =========================
@st.cache_data(ttl=120)
def run_query(sql: str) -> pd.DataFrame:
    conn = connect(
        s3_staging_dir=S3_STAGING_DIR,
        region_name=REGION,
        schema_name=DATABASE,
    )
    return pd.read_sql(sql, conn)


def sentiment_color(sent):
    return {
        "Very Positive": "🟢",
        "Positive": "🟢",
        "Neutral": "🟡",
        "Negative": "🔴",
        "Very Negative": "🔴",
    }.get(sent, "⚪")


# =========================
# Página
# =========================
st.set_page_config(
    page_title="Mastodon Sentiment Intelligence",
    layout="wide",
)

st.title("🧠 Mastodon Sentiment Intelligence Dashboard")

st.markdown(
    """
**Análisis de sentimiento multilingüe en tiempo (casi) real sobre Mastodon.**

Este dashboard monitoriza publicaciones públicas capturadas vía *streaming* y procesadas
mediante **modelos de lenguaje de Hugging Face**, clasificando cada mensaje por sentimiento
y asignándole un **score de confianza**.

Autor: Julio Úbeda Quesada
"""
)

st.divider()

# =========================
# Filtros
# =========================
dt_sql = f"""
SELECT DISTINCT dt
FROM {DATABASE}.{TABLE}
ORDER BY dt
"""
dt_df = run_query(dt_sql)

dt_dates = pd.to_datetime(dt_df["dt"]).dt.date.tolist()
min_dt, max_dt = min(dt_dates), max(dt_dates)

lang_sql = f"""
SELECT DISTINCT lang
FROM {DATABASE}.{TABLE}
WHERE lang IS NOT NULL AND lang <> ''
ORDER BY lang
"""
lang_df = run_query(lang_sql)
lang_options = ["All"] + lang_df["lang"].tolist()

st.subheader("🎛️ Filtros de análisis")

c1, c2 = st.columns([2, 1])

with c1:
    dt_range = st.slider(
        "Rango temporal",
        min_value=min_dt,
        max_value=max_dt,
        value=(min_dt, max_dt),
        format="YYYY-MM-DD",
    )

with c2:
    selected_lang = st.selectbox("Idioma", lang_options)

date_from, date_to = dt_range
where = [f"dt BETWEEN '{date_from}' AND '{date_to}'"]
if selected_lang != "All":
    where.append(f"lang = '{selected_lang}'")
where_sql = " AND ".join(where)

# =========================
# KPIs globales
# =========================
kpi_sql = f"""
SELECT
    COUNT(*) AS total_posts,
    COUNT(DISTINCT lang) AS total_languages,
    ROUND(AVG(sentiment_score), 4) AS avg_score,
    ROUND(STDDEV(sentiment_score), 4) AS volatility
FROM {DATABASE}.{TABLE}
WHERE {where_sql}
"""
kpi = run_query(kpi_sql).iloc[0]

st.subheader("📊 Indicadores clave")

k1, k2, k3, k4 = st.columns(4)

k1.metric("Posts analizados", f"{int(kpi.total_posts):,}")
k2.metric("Idiomas detectados", int(kpi.total_languages))
k3.metric("Score medio", kpi.avg_score)
k4.metric("Volatilidad emocional", kpi.volatility)

st.caption(
    "La volatilidad mide la dispersión del sentimiento: valores altos indican mayor polarización emocional."
)

st.divider()

# =========================
# Distribución de sentimiento
# =========================
dist_sql = f"""
SELECT sentiment, COUNT(*) AS total
FROM {DATABASE}.{TABLE}
WHERE {where_sql}
GROUP BY sentiment
ORDER BY total DESC
"""
dist = run_query(dist_sql)

st.subheader("🙂 Distribución emocional")

c1, c2 = st.columns([1, 1])

with c1:
    dist["sentiment_label"] = dist["sentiment"].apply(sentiment_color) + " " + dist["sentiment"] # type: ignore
    st.dataframe(
        dist[["sentiment_label", "total"]],
        use_container_width=True,
        hide_index=True,
    )

with c2:
    fig = plt.figure(figsize=(6, 4))
    plt.pie(
        dist["total"],
        labels=dist["sentiment"], # type: ignore
        autopct="%1.1f%%",
        startangle=90,
    )
    plt.axis("equal")
    st.pyplot(fig)

st.divider()

# =========================
# Balance emocional
# =========================
balance_sql = f"""
SELECT
    SUM(CASE WHEN sentiment IN ('Very Positive', 'Positive') THEN 1 ELSE 0 END) -
    SUM(CASE WHEN sentiment IN ('Negative', 'Very Negative') THEN 1 ELSE 0 END)
    AS emotional_balance
FROM {DATABASE}.{TABLE}
WHERE {where_sql}
"""
balance = run_query(balance_sql).iloc[0]["emotional_balance"]

st.subheader("⚖️ Balance emocional global")
st.metric(
    "Positivo – Negativo",
    int(balance),
    help="Indicador sintético del clima emocional general",
)

st.divider()

# =========================
# Evolución temporal
# =========================
trend_sql = f"""
SELECT dt, sentiment, COUNT(*) AS total
FROM {DATABASE}.{TABLE}
WHERE {where_sql}
GROUP BY dt, sentiment
ORDER BY dt
"""
trend = run_query(trend_sql)

st.subheader("📈 Evolución del sentimiento en el tiempo")

pivot = (
    trend.pivot_table(
        index="dt",
        columns="sentiment",
        values="total",
        aggfunc="sum",
    )
    .fillna(0)
    .sort_index()
)

fig = plt.figure(figsize=(9, 4))
for col in pivot.columns:
    plt.plot(pivot.index, pivot[col], marker="o", label=col)

plt.legend()
plt.xlabel("Fecha")
plt.ylabel("Número de publicaciones")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

st.divider()

# =========================
# Evidencia cualitativa
# =========================
st.subheader("🧾 Ejemplos representativos (mayor score por sentimiento)")

examples_sql = f"""
SELECT sentiment, sentiment_score, lang, text, url
FROM (
  SELECT
    sentiment,
    sentiment_score,
    lang,
    text,
    url,
    ROW_NUMBER() OVER (
      PARTITION BY sentiment
      ORDER BY sentiment_score DESC
    ) AS rn
  FROM {DATABASE}.{TABLE}
  WHERE {where_sql}
)
WHERE rn = 1
ORDER BY sentiment
"""
examples = run_query(examples_sql)

st.dataframe(examples, use_container_width=True)

st.divider()

# =========================
# Información del modelo
# =========================
st.subheader("🤖 Motor de análisis de sentimiento")

engine_sql = f"""
SELECT sentiment_engine, COUNT(*) AS total
FROM {DATABASE}.{TABLE}
WHERE {where_sql}
GROUP BY sentiment_engine
"""
engine = run_query(engine_sql)

st.markdown(
    """
Este sistema utiliza **modelos de lenguaje multilingües de Hugging Face**
para clasificar automáticamente el sentimiento de cada publicación,
permitiendo analizar conversaciones en **decenas de idiomas con un único pipeline de IA**.
"""
)

st.dataframe(engine, use_container_width=True)
