import requests
from txt2sql_model import Qwen2Txt2SQL

SERVER_URL = "http://localhost:8000"  # ajuste se necessário

def get_schema():
    resp = requests.get(f"{SERVER_URL}/tools/get-schema")
    return resp.json()

def execute_query(sql_query):
    resp = requests.post(f"{SERVER_URL}/tools/execute-query", json={"query": sql_query})
    return resp.json()

def main():
    user_question = input("Pergunta sobre o banco: ")
    schema = get_schema()
    sql_query = Qwen2Txt2SQL.generate_sql(user_question, schema)
    print(f"Query SQL gerada: {sql_query}")
    result = execute_query(sql_query)
    print("Resultado:")
    print(result)

if __name__ == "__main__":
    main()