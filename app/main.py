import os
import pymysql
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

# .envファイルから環境変数を読み込み
load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!!!!!!!11111111111"}

@app.get("/db-health")
def check_database_connection():
    try:
        host = os.getenv("DB_HOST", "db")
        port = int(os.getenv("DB_PORT", "3306"))
        username = os.getenv("DB_USER", "root")
        password = os.getenv("DB_PASSWORD", "password")
        database = os.getenv("DB_NAME", "sampledb")
        
        connection = pymysql.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database=database,
            charset='utf8mb4'
        )
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
        
        connection.close()
        
        return {
            "status": "success",
            "message": "MySQL connection successful",
            "host": host,
            "port": port,
            "database": database,
            "test_query_result": result
        }
        
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Database connection failed: {str(error)}"
        )
