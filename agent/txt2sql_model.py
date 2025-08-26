import ollama

class Qwen2Txt2SQL:
    @staticmethod
    def generate_sql(user_question, schema):
        system_prompt = (
            "Receba uma pergunta em linguagem natural e o schema do banco de dados. "
            "Retorne APENAS a query SQL correspondente, sem comentários ou explicações."
        )
        prompt = f"{system_prompt}\nPergunta: {user_question}\nSchema: {schema}"
        response = ollama.chat(model="qwen2", messages=[{"role": "user", "content": prompt}])
        
        sql_query = response['message']['content'].strip()
        return sql_query