import requests
from server.config import MINIO_URL

# MinIO 서버에서 파일을 가져오는 기능을 제공

def fetch_file(filename: str) -> str:
    res = requests.get(f"{MINIO_URL}/{filename}") # MinIO 서버에서 파일을 GET 요청으로 가져옴
    res.raise_for_status()  # 실패 시 예외 발생
    return res.text # 파일의 내용을 텍스트로 반환