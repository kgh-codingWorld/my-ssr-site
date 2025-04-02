import os
from dotenv import load_dotenv

load_dotenv()

MINIO_URL = os.getenv("MINIO_URL")

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_CACHE_TTL = int(os.getenv("REDIS_CACHE_TTL", 300))