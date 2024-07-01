import asyncpg
import asyncio

# Configuração do banco de dados PostgreSQL
DATABASE_URL = "postgresql://banco:@banco.postgres.database.azure.com:5432/postgres?sslmode=require&password=@Senhaforte100"

# Função para conectar ao banco de dados
async def test_db_connection():
    try:
        # Conectar ao banco de dados
        conn = await asyncpg.connect(DATABASE_URL)
        await conn.close()
        print("Conexão bem-sucedida!")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {str(e)}")

# Executar o teste de conexão
if __name__ == "__main__":
    asyncio.run(test_db_connection())
