import requests
from server.config import MINIO_URL

def fetch_file(filename: str) -> str:
    res = requests.get(f"{MINIO_URL}/{filename}")
    res.raise_for_status()  # 실패 시 예외 발생
    return res.text