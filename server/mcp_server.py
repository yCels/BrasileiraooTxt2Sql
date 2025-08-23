# server/mcp_server.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .services import execute_sql_query, get_database_schema

app = FastAPI(title="Servidor de Ferramentas de Banco de Dados")

class QueryRequest(BaseModel):
    query: str

# Use startup_event para executar código durante a inicialização
@app.on_event("startup")
async def startup_event():
    print("O servidor foi iniciado!")
    print("Acesse a documentação interativa em http://127.0.0.1:8000/docs")

# Endpoint de verificação de status
@app.get("/health")
def health_check():
    """Verifica se o servidor está funcionando."""
    return {"status": "ok", "message": "Servidor está online!"}

# Endpoint para executar qualquer query
@app.post("/tools/execute-query")
def execute_query_tool(request: QueryRequest):
    """Executa uma query SQL no banco de dados e retorna o resultado."""
    result, error = execute_sql_query(request.query)
    
    if error:
        raise HTTPException(status_code=400, detail=error)
    
    return {"status": "success", "result": result}

# Endpoint para obter o schema do banco de dados
@app.post("/tools/get-schema")
def get_schema_tool():
    """Retorna o schema completo do banco de dados."""
    schema, error = get_database_schema()
    
    if error:
        raise HTTPException(status_code=500, detail=error)
    
    return {"status": "success", "schema": schema}