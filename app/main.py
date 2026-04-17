from fastapi import FastAPI, HTTPException
from app.schemas import (
    AskRequest,
    AskResponse,
    QueryResponse,
    ExplainDataRequest,
)
from app.services.openai_service import ask_openai, explain_data_with_ai
from app.services.db_service import execute_query
from app.config import OPENAI_MODEL
from app.services.dataset_service import ALLOWED_DATASETS
from app.schemas import DatasetExplainRequest

app = FastAPI(
    title="Mi API de IA",
    version="1.0.0",
    description="API simple en Python que consume OpenAI y SQL Server"
)


@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    try:
        result = ask_openai(request.prompt)
        return AskResponse(response=result, model=OPENAI_MODEL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/clientes", response_model=QueryResponse)
def get_clientes():
    try:
        query = """
        SELECT TOP 10
            SK_CLI_Cliente,
            CD_ID_Origen,
            VC_CLI_RazonSocial
        FROM dbo.LK_Cliente
        ORDER BY SK_CLI_Cliente DESC
        """
        rows = execute_query(query)
        return QueryResponse(rows=rows)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/clientes/explicar", response_model=AskResponse)
def explain_clientes(request: ExplainDataRequest):
    try:
        query = """
        SELECT TOP 10
            SK_CLI_Cliente,
            CD_ID_Origen,
            VC_CLI_RazonSocial
        FROM dbo.LK_Cliente
        ORDER BY SK_CLI_Cliente DESC
        """
        rows = execute_query(query)
        explanation = explain_data_with_ai(request.prompt, rows)
        return AskResponse(response=explanation, model=OPENAI_MODEL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/indicadores/explicar", response_model=AskResponse)
def explain_dataset(request: DatasetExplainRequest):
    try:
        if request.dataset not in ALLOWED_DATASETS:
            raise HTTPException(status_code=400, detail="Dataset no permitido")

        query = ALLOWED_DATASETS[request.dataset]
        rows = execute_query(query)

        explanation = explain_data_with_ai(request.prompt, rows)

        return AskResponse(response=explanation, model=OPENAI_MODEL)

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))