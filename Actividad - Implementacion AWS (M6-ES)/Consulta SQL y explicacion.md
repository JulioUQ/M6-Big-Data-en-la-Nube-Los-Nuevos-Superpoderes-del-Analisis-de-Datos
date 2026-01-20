# 📊 Mastodon Sentiment Analysis – Documentación SQL

## 1️⃣ Creación de la base de datos

```sql
CREATE DATABASE IF NOT EXISTS MastodonAnalysis;
```

### 📌 ¿Por qué se hace?

- Crea un **namespace lógico** donde agrupar todas las tablas relacionadas con el análisis de Mastodon.
- Evita conflictos con otras bases de datos.
- `IF NOT EXISTS` hace la operación **idempotente**, evitando errores si la base ya existe.

---

## 2️⃣ Definición de la tabla externa

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS MastodonAnalysis.mastodon_sentiment (
  source string,
  id string,
  created_at string,
  lang string,
  text string,
  acct string,
  url string,
  tags array<string>,
  ingest_ts string,
  raw_ingest_ts string,
  sentiment string,
  sentiment_score double,
  processed_ts string,
  sentiment_engine string
)
PARTITIONED BY (dt string)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://bucketmastodonjubedaq/processeddata/mastodon_sentiment_analysis/'
TBLPROPERTIES ('has_encrypted_data'='false');
```

### 📌 ¿Por qué se hace?

Este bloque **define la estructura lógica** de los datos almacenados en S3 para que puedan ser consultados desde **Athena / Glue** sin mover los ficheros.

---

## 3️⃣ Campos de la tabla

### 🔹 Metadatos del post

|Campo|Descripción|
|---|---|
|`source`|Origen del dato (stream, batch, API, etc.)|
|`id`|Identificador único del post|
|`created_at`|Fecha/hora de creación del post|
|`lang`|Idioma detectado|
|`text`|Contenido textual del post|
|`acct`|Cuenta del autor|
|`url`|URL del post|
|`tags`|Lista de hashtags|

---

### 🔹 Metadatos de ingestión

|Campo|Descripción|
|---|---|
|`ingest_ts`|Timestamp de ingestión procesada|
|`raw_ingest_ts`|Timestamp original del evento|
|`processed_ts`|Timestamp del análisis de sentimiento|
|`source`|Pipeline o proceso de origen|

---

### 🔹 Resultados del análisis de sentimiento

|Campo|Descripción|
|---|---|
|`sentiment`|Etiqueta del sentimiento (POSITIVE / NEGATIVE / NEUTRAL)|
|`sentiment_score`|Score numérico del modelo|
|`sentiment_engine`|Motor o modelo usado (ej: HuggingFace)|

---

### 🔹 Partición

|Campo|Descripción|
|---|---|
|`dt`|Fecha lógica (YYYY-MM-DD) usada para particionar|

📌 **Ventaja de la partición**

- Reduce costes
- Mejora el rendimiento
- Permite filtrar por fechas de forma eficiente

---

## 4️⃣ Reparación de particiones

```sql
MSCK REPAIR TABLE MastodonAnalysis.mastodon_sentiment;
```

### 📌 ¿Por qué se hace?

- Detecta automáticamente las carpetas `dt=YYYY-MM-DD` en S3.
- Registra las particiones en el metastore.
- **Imprescindible** cuando las particiones se crean fuera de Athena (ETL, Lambda, Glue).

---

## 5️⃣ Consulta de validación rápida

```sql
SELECT *
FROM MastodonAnalysis.mastodon_sentiment
LIMIT 10;
```

### 📌 ¿Por qué se hace?

- Verifica que la tabla:
    
    - Existe
    - Lee correctamente el JSON
    - Tiene datos accesibles

- Útil como **smoke test** inicial

---

## 6️⃣ Consulta de métricas globales (Overview analítico)

```sql
SELECT
    COUNT(*)                                      AS total_posts,
    COUNT(DISTINCT dt)                            AS total_days,
    MIN(dt)                                       AS first_dt,
    MAX(dt)                                       AS last_dt,

    COUNT(DISTINCT lang)                          AS total_languages,
    COUNT(DISTINCT sentiment)                     AS total_sentiments,

    -- Calidad de datos
    SUM(CASE WHEN sentiment IS NULL THEN 1 ELSE 0 END)        AS null_sentiment,
    SUM(CASE WHEN sentiment_score IS NULL THEN 1 ELSE 0 END)  AS null_score,
    SUM(CASE WHEN text IS NULL OR text = '' THEN 1 ELSE 0 END) AS empty_text,

    -- Métricas del score
    ROUND(AVG(sentiment_score), 4)                AS avg_score,
    ROUND(MIN(sentiment_score), 4)                AS min_score,
    ROUND(MAX(sentiment_score), 4)                AS max_score,
    ROUND(STDDEV(sentiment_score), 4)             AS stddev_score

FROM MastodonAnalysis.mastodon_sentiment;
```

### 📌 ¿Por qué se hace?

Esta consulta da una **visión ejecutiva del dataset**:

#### 🔹 Volumen y cobertura temporal

- ¿Cuántos posts se analizan?
- ¿Cuántos días cubre el histórico?
- ¿Desde cuándo hasta cuándo hay datos?

#### 🔹 Diversidad

- Idiomas reales capturados
- Etiquetas de sentimiento existentes

#### 🔹 Calidad del dato

- Posts sin sentimiento
- Scores nulos
- Textos vacíos

#### 🔹 Comportamiento del modelo

- Media, mínimo y máximo del score
- Dispersión del modelo (STDDEV)
---

## 7️⃣ Distribución temporal del sentimiento

```sql
SELECT
    dt,
    sentiment,
    COUNT(*) AS total
FROM MastodonAnalysis.mastodon_sentiment
GROUP BY dt, sentiment
ORDER BY dt, total DESC;
```

### 📌 ¿Por qué se hace?

- Analiza la **evolución temporal del sentimiento**
- Permite:
    - Detectar picos emocionales
    - Analizar eventos
    - Construir dashboards (QuickSight, Superset, etc.)

📈 Ideal para gráficas tipo:

- Stacked bars por día
- Tendencias de polarización
- Series temporales

