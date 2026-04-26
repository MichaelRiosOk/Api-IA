# API IA + Data Warehouse

API desarrollada en Python que integra **FastAPI, SQL Server y OpenAI** para consultar datos de un Data Warehouse y generar automáticamente **análisis de negocio en lenguaje natural con formato ejecutivo**.

---

## 🎯 Objetivo

Permitir transformar datos operativos en **insights accionables**, evitando consultas manuales complejas y facilitando la interpretación para perfiles de negocio.

---

## 🧱 Arquitectura

```
[ Cliente / Usuario ]
          │
          ▼
      FastAPI
          │
 ┌────────┴────────┐
 ▼                 ▼
SQL Server      OpenAI API
(DWH - Vistas)   (IA)
```

* **FastAPI**: expone endpoints REST
* **SQL Server**: fuente de datos (vistas curadas)
* **OpenAI**: generación de análisis e insights

---

## ⚙️ Tecnologías utilizadas

* Python
* FastAPI
* OpenAI API
* SQL Server
* pyodbc
* dotenv

---

## 🔐 Seguridad y diseño

Este proyecto sigue buenas prácticas de arquitectura:

* ❌ No expone el Data Warehouse completo
* ✅ Uso de **datasets controlados (vistas SQL)**
* ❌ No permite SQL dinámico desde el usuario
* ✅ Control de volumen de datos (TOP, agregaciones)
* ✅ Uso de variables de entorno para credenciales
* ✅ Separación de capas (API / Data / IA)

---

## 📊 Datasets disponibles

La API trabaja únicamente con datasets autorizados:

* `ot_por_estado` → distribución de órdenes de trabajo
* `ot_tiempos` → tiempos del proceso operativo
* `casos_sucursal_familia` → reclamos por sucursal y producto

Estos datasets provienen de vistas SQL agregadas para optimizar performance y costos.

---

## 📡 Endpoints principales

### 🔹 Obtener datos sin IA

```
GET /indicadores/{dataset}
```

Ejemplo:

```
GET /indicadores/ot_por_estado
```

---

### 🔹 Generar análisis con IA

```
POST /indicadores/explicar
```

#### Body:

```json
{
  "dataset": "ot_por_estado",
  "prompt": "Analiza la distribución de órdenes de trabajo por región y identifica oportunidades de expansión"
}
```

#### Respuesta:

* Resumen ejecutivo
* Hallazgos principales
* Alertas
* Conclusión

---

## 🧠 Ejemplo de salida

```
Resumen ejecutivo:
La distribución de órdenes de trabajo revela patrones claros de demanda regional, con oportunidades de expansión estratégica.

Hallazgos:
- Región A concentra el 40% del volumen total, indicando alta actividad operativa.
- Se observa un crecimiento del 15% en órdenes mensuales en las últimas semanas.
- Región B muestra potencial de escalabilidad con bajo volumen actual.

Conclusión:
Ideal para priorizar inversiones en logística y optimizar la asignación de recursos en mercados clave.
```

---

## 🛠️ Instalación

```bash
git clone <repo>
cd api-ia

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
```

---

## 🔑 Variables de entorno

Crear archivo `.env`:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-5.4

SQL_SERVER=your_server
SQL_DATABASE=your_database
SQL_USERNAME=your_user
SQL_PASSWORD=your_password
SQL_DRIVER=ODBC Driver 17 for SQL Server
```

---

## ▶️ Ejecutar la API

```bash
uvicorn app.main:app --reload
```

Acceder a:

👉 http://127.0.0.1:8000/docs

---

## 💡 Casos de uso

* Análisis de órdenes de trabajo (EAM)
* Seguimiento de reclamos (Salesforce)
* Evaluación de performance operativa
* Generación automática de reportes ejecutivos
* Soporte a toma de decisiones

---

## 📌 Notas

* Este proyecto no incluye datos reales productivos
* Las vistas utilizadas son representativas
* Las credenciales deben configurarse localmente

---

## 📈 Próximas mejoras

* Selección automática de dataset según pregunta (IA)
* Detección de anomalías
* Integración con dashboards (Power BI / Streamlit)
* Exportación de reportes

---

## 👨‍💻 Autor

Proyecto desarrollado como iniciativa de **Data Engineering + AI aplicada a negocio**.

---
