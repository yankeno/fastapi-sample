import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# .envファイルから環境変数を読み込み
load_dotenv()

def get_database_url():
    """
    データベースURLを取得する

    Returns:
        str: データベース接続URL
    """
    host = os.getenv("DB_HOST", "db")
    port = os.getenv("DB_PORT", "3306")
    username = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "password")
    database = os.getenv("DB_NAME", "sampledb")

    return f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset=utf8mb4"

# データベースエンジンの作成
engine = create_engine(get_database_url())

# セッションローカルクラスの作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ベースクラスの作成
Base = declarative_base()

def get_database_session():
    """
    データベースセッションを取得する

    Returns:
        SessionLocal: SQLAlchemyセッションオブジェクト
    """
    return SessionLocal()

def get_database_connection():
    """
    データベース接続を取得する（生のコネクション）

    Returns:
        Connection: SQLAlchemyコネクションオブジェクト
    """
    return engine.connect()
