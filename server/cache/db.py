import psycopg2 # 파이썬에서 PostgreSQL을 연결해줌
from server.config import PG_CONFIG # .env랑 연결되어 있는 config.py에서 실제 DB 설정값 가져옴

# PostgresSQL 연결 함수
def get_pg_connection():
    return psycopg2.connect(**PG_CONFIG)
