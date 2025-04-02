from datetime import datetime, timedelta
from server.cache.pg_util import execute_one, execute_write

def get_cache(key: str) -> str | None:
    row = execute_one(
        "SELECT content FROM cache WHERE key = %s AND expires_at > NOW()",
        (key,)
    )
    return row[0] if row else None

def set_cache(key: str, content: str, ttl: int = 300):
    expires_at = datetime.utcnow() + timedelta(seconds=ttl)
    execute_write(
        """
        INSERT INTO cache(key, content, expires_at)
        VALUES(%s, %s, %s)
        ON CONFLICT(key)
        DO UPDATE SET content = EXCLUDED.content, expires_at = EXCLUDED.expires_at
        """,
        (key, content, expires_at)
    )
# ON CONFLICT(key) : key가 이미 존재하면 충돌로 간주
# DO UPDATE SET... : 충돌 시 기존 row를 다음 값으로 갱신
# expires_at = EXCLUDED.expires_at : 만료시간을 새 TTL로 갱신