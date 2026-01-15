import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from pyathena import connect

REGION = "us-east-1"
S3_STAGING_DIR = "s3://bucketmastodonjubedaq/athena/"  # <-- ajusta si hace falta
DATABASE = "MastodonAnalysis"
TABLE = "mastodon_sentiment"

@st.cache_data(ttl=120)
def run_query(sql: str) -> pd.DataFrame:
    conn = connect(
        s3_staging_dir=S3_STAGING_DIR,
        region_name=REGION,
        schema_name=DATABASE,
    )
    return pd.read_sql(sql, conn)

st.set_page_config(page_title="Mastodon Sentiment Dashboard", layout="wide")
st.title("Mastodon Sentiment Dashboard")

# =========================
# 1) Dominios de filtros (dt e idiomas)
# =========================
dt_sql = f"""
SELECT DISTINCT dt
FROM {DATABASE}.{TABLE}
WHERE dt IS NOT NULL
ORDER BY dt
"""
dt_df = run_query(dt_sql)

if dt_df.empty:
    st.error('No hay particiones "dt" disponibles. Ejecuta MSCK REPAIR TABLE y asegúrate de que existan datos.')
    st.stop()

dt_list = dt_df["dt"].dropna().astype(str).tolist()
dt_dates = pd.to_datetime(dt_list).date.tolist()
min_dt, max_dt = min(dt_dates), max(dt_dates)

lang_sql = f"""
SELECT DISTINCT lang
FROM {DATABASE}.{TABLE}
WHERE lang IS NOT NULL AND lang <> ''
ORDER BY lang
"""
lang_df = run_query(lang_sql)
lang_options = ["All"] + (lang_df["lang"].dropna().astype(str).tolist() if not lang_df.empty else [])

# =========================
# 2) UI de filtros
# =========================
st.subheader("Filtros")
c1, c2 = st.columns([2, 1])

with c1:
    if min_dt == max_dt:
        dt_range = (min_dt, max_dt)
        st.info(f"Solo hay datos para {min_dt.isoformat()}")
    else:
        dt_range = st.slider(
            "Rango de fechas (dt)",
            min_value=min_dt,
            max_value=max_dt,
            value=(min_dt, max_dt),
            format="YYYY-MM-DD",
        )

with c2:
    selected_lang = st.selectbox("Idioma", options=lang_options, index=0)

date_from, date_to = dt_range
date_from_str = date_from.isoformat()
date_to_str = date_to.isoformat()

where = [f"dt BETWEEN '{date_from_str}' AND '{date_to_str}'"]
if selected_lang != "All":
    where.append(f"lang = '{selected_lang}'")
where_sql = " AND ".join(where)

# =========================
# 3) KPI total
# =========================
kpi_sql = f"""
SELECT COUNT(*) AS total_posts
FROM {DATABASE}.{TABLE}
WHERE {where_sql}
"""
kpi = run_query(kpi_sql).iloc[0]["total_posts"]
st.metric("Total posts", int(kpi))

# =========================
# 4) Bar chart arriba: total por sentimiento (ajustado)
# =========================
st.subheader("Total por sentimiento (conteo)")

total_bar_sql = f"""
SELECT sentiment, COUNT(*) AS total
FROM {DATABASE}.{TABLE}
WHERE {where_sql}
GROUP BY sentiment
ORDER BY total DESC
"""
total_bar = run_query(total_bar_sql)

fig0 = plt.figure(figsize=(6, 3))
plt.bar(total_bar["sentiment"], total_bar["total"])
plt.xticks(rotation=30, ha="right")
plt.xlabel("Sentiment")
plt.ylabel("Total")
plt.tight_layout()
st.pyplot(fig0)

st.divider()

# =========================
# 5) Distribución + pie
# =========================
st.subheader("Distribución de sentimiento")

dist = total_bar.copy()  # misma query, mismo resultado
left, right = st.columns([1, 1])

with left:
    st.dataframe(dist, use_container_width=True)

with right:
    fig = plt.figure(figsize=(6, 3))
    plt.pie(dist["total"], labels=dist["sentiment"], autopct="%1.1f%%")
    plt.axis("equal")
    plt.tight_layout()
    st.pyplot(fig)

st.divider()

# =========================
# 6) Evolución por día + líneas múltiples (eje X igual que tabla dt)
# =========================
st.subheader("Evolución por día (conteos)")

trend_sql = f"""
SELECT dt, sentiment, COUNT(*) AS total
FROM {DATABASE}.{TABLE}
WHERE {where_sql}
GROUP BY dt, sentiment
ORDER BY dt
"""
trend = run_query(trend_sql)

st.dataframe(trend, use_container_width=True)

if not trend.empty:
    trend_pivot = trend.copy()
    trend_pivot["dt"] = trend_pivot["dt"].astype(str)  # igual que la tabla
    pivot = (
        trend_pivot
        .pivot_table(index="dt", columns="sentiment", values="total", aggfunc="sum")
        .fillna(0)
        .sort_index()
    )

    fig2 = plt.figure(figsize=(8, 3))
    for col in pivot.columns:
        plt.plot(pivot.index, pivot[col], marker="o", label=str(col))
    plt.legend()
    plt.xlabel("dt")
    plt.ylabel("Total")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(fig2)

st.divider()

# =========================
# 7) Ejemplo con mayor score por sentimiento
# =========================
st.subheader("Ejemplo con mayor score por sentimiento")

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
    AND sentiment_score IS NOT NULL
)
WHERE rn = 1
ORDER BY sentiment
"""
examples = run_query(examples_sql)
st.dataframe(examples, use_container_width=True)

# =========================
# 8) Descargas
# =========================
st.divider()
st.subheader("Descargar resultados")

st.download_button(
    "Descargar distribución (CSV)",
    dist.to_csv(index=False).encode("utf-8"),
    "sentiment_distribution.csv",
)
st.download_button(
    "Descargar tendencia (CSV)",
    trend.to_csv(index=False).encode("utf-8"),
    "sentiment_trend.csv",
)
st.download_button(
    "Descargar ejemplos (CSV)",
    examples.to_csv(index=False).encode("utf-8"),
    "sentiment_examples.csv",
)