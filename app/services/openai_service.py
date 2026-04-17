import json
from openai import OpenAI
from app.config import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)


def ask_openai(prompt: str) -> str:
    response = client.responses.create(
        model=OPENAI_MODEL,
        instructions="Respondé de forma clara y útil en español.",
        input=prompt,
    )
    return response.output_text


def explain_data_with_ai(user_prompt: str, data: list[dict]) -> str:
    import json

    data_text = json.dumps(data, default=str, ensure_ascii=False)

    prompt = f"""
Sos un analista senior de datos orientado a operaciones y negocio.
Tenés que responder con criterio ejecutivo, de forma clara, concreta y profesional.

Pregunta del usuario:
{user_prompt}

Datos disponibles:
{data_text}

Reglas:
- Respondé en español.
- Basate únicamente en los datos recibidos.
- No inventes causas ni afirmes conclusiones que no se desprendan del recorte.
- Si algo surge solo del recorte consultado, aclaralo con frases como:
  "en los datos analizados" o "en el recorte consultado".
- Si detectás valores '*sin dato*', tratalo como alerta de calidad de datos.
- Si hay meses, compará tendencias solo si realmente aparecen en los datos.
- Si hay estados o categorías dominantes, destacalos.
- Si hay métricas bajas de facturación o cierre, mencionarlo como observación, no como afirmación absoluta del negocio.
- Evitá repetir todos los valores uno por uno salvo los más relevantes.

Formato de salida obligatorio:

Resumen ejecutivo:
- 2 a 3 líneas con la lectura principal.

Hallazgos principales:
- 4 bullets máximo.
- Priorizar concentración, tendencia, desvíos y comparaciones relevantes.

Alertas o puntos de atención:
- 2 bullets máximo.
- Incluir calidad de datos si aplica.

Conclusión:
- 1 a 2 líneas con interpretación de negocio prudente.
"""
    response = client.responses.create(
        model=OPENAI_MODEL,
        input=prompt,
    )

    return response.output_text