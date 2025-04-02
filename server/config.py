import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

MINIO_URL = os.getenv("MINIO_URL")

PG_CONFIG = {
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT"),
    "dbname": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
}