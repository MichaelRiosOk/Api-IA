from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    prompt: str = Field(..., min_length=1, description="Texto enviado por el usuario")


class AskResponse(BaseModel):
    response: str
    model: str


class QueryResponse(BaseModel):
    rows: list


class ExplainDataRequest(BaseModel):
    prompt: str = Field(..., min_length=1, description="Pregunta sobre los datos")
    

class DatasetExplainRequest(BaseModel):
    dataset: str
    prompt: str