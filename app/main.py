from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from database import get_database_connection, get_database_session

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/db-health")
def check_database_connection():
    try:
        connection = get_database_connection()

        # SQLAlchemyの生コネクションでSQLを実行
        result = connection.execute(text("SELECT 1")).fetchone()
        connection.close()

        return {
            "status": "success",
            "message": "MySQL connection successful",
            "test_query_result": result[0] if result else None
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Database connection failed: {str(error)}"
        )
