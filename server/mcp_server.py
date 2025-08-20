import sqlite3
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("mcp-server")

# Ferramenta para adicionar dados
@mcp.tool()
def add_data(query: str) -> bool:
    """Executa uma query INSERT para adicionar um registro."""
    conn = sqlite3.connect("database.db") 
    conn.execute(query)
    conn.commit()
    conn.close()
    return True

# Ferramenta para ler dados
@mcp.tool()
def read_data(query: str = "SELECT * FROM registros") -> list:
    """Executa uma query SELECT e retorna todos os registros."""
    conn = sqlite3.connect("database.db")  
    results = conn.execute(query).fetchall()
    conn.close()
    return results

# Inicia o servidor
if __name__ == "__main__":
    print("🚀 Iniciando o servidor MCP... ")
    mcp.run()  # OOOO Moreira lembrar de ver se o servidor está iniciado