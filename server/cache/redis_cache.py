import redis
from server.config import REDIS_HOST, REDIS_PORT

# Redis 서버와 애플리케이션 간의 연결을 설정하고, 데이터를 캐싱하는 기능을 제공하는 파일

cache = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True # Redis에서 가져온 응답을 자동으로 디코딩하여 문자열로 반환하도록 설정
)
