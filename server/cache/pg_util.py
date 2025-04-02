from server.cache.db import get_pg_connection # PostgresSQL 연결 함수

# 단일 결과값만 가져오는 쿼리 실행 함수
def execute_one(query: str, params: tuple = ()): 
    conn = get_pg_connection()
    with conn: # with 블록을 사용해 커넥션 자동 종료 보장
        with conn.cursor() as cur: # 커서 생성(SQL 실행 도구)
            cur.execute(query, params) # SQL 실행
            return cur.fetchone() # 한 개의 row만 가져오고 없으면 None
# 쓰기 쿼리 실행 함수
def execute_write(query: str, params: tuple = ()): 
    conn = get_pg_connection()
    with conn: # 자동 커밋 블록
        with conn.cursor() as cur: # 커서 생성
            cur.execute(query, params) # 쓰기 전용이라 반환값 없음
