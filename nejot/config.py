import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "YOUR_GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID", "YOUR_GOOGLE_CSE_ID")

EMBEDDING_CACHE_FILE = "DB_embedding/1212_2차_embedding.pt"

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),    # 기본값 "localhost"
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "db": os.getenv("DB_NAME", "test"),
    # 이모티콘(4바이트 문자)도 저장하기 위해 utf8mb4 권장
    "charset": "utf8mb4"
}