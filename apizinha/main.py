# main.py

from fastapi import FastAPI, HTTPException
import asyncpg
from typing import List

app = FastAPI()

# Configurações do banco de dados PostgreSQL
DATABASE_URL = "postgresql://banco:@banco.postgres.database.azure.com:5432/postgres?sslmode=require&password=@Senhaforte100"

# Função para conectar ao banco de dados
async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL)

# Rota GET para buscar dados no banco de dados
@app.get("/items", response_model=List[dict])
async def get_items():
    query = "select c.data, c.ultimo as valor from public.cotacao c ;;"  # Substitua pela sua consulta SQL
    try:
        conn = await connect_to_db()
        rows = await conn.fetch(query)
        await conn.close()
        return [dict(row) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

