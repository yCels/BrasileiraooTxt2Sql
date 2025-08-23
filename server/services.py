# server/services.py
import sqlite3

DB_PATH = "./server/data/brasileirao.db"

def get_db_connection():
    """Função auxiliar para obter uma conexão com o banco de dados."""
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        print(f"Erro de conexão com o banco de dados: {e}")
        return None

def execute_sql_query(query: str):
    """Executa uma query SQL e retorna o resultado ou um status."""
    conn = get_db_connection()
    if not conn:
        return None, "Erro ao conectar com o banco de dados."
    
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        
        if query.strip().upper().startswith("SELECT"):
            results = cursor.fetchall()
            conn.close()
            return results, None
        else:
            conn.commit()
            conn.close()
            return "Query executada com sucesso.", None

    except sqlite3.Error as e:
        conn.close()
        return None, f"Erro na query SQL: {e}"

def get_database_schema():
    """Retorna o schema completo do banco de dados como uma string."""
    conn = get_db_connection()
    if not conn:
        return None, "Erro ao conectar com o banco de dados."
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        schema_str = "Schema do Banco de Dados:\n"
        for table in tables:
            table_name = table[0]
            schema_str += f"\nTabela: {table_name}\n"
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            for col in columns:
                schema_str += f"  - Coluna: {col[1]} (Tipo: {col[2]})\n"
        conn.close()
        return schema_str, None
    except sqlite3.Error as e:
        conn.close()
        return None, f"Erro ao obter o schema: {e}"