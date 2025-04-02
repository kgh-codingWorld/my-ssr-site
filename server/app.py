from flask import Flask, Response
import requests
import time
from server.cache.pg_cache import get_cache, set_cache
from server.utils.file_util import fetch_file
from server.log.logger import logging

app = Flask(__name__)

@app.route("/")
def index():
    start = time.time()
    # 캐시 키
    cache_key = "page:index"

    # 캐시에 존재
    cached_html = get_cache(cache_key)
    if cached_html:
        duration = time.time() - start
        logging.info(f"✅ PostgreSQL Cache HIT: {duration:.4f}초")
        return Response(cached_html, mimetype="text/html")
    
    logging.info("❌ PostgreSQL Cache MISS")
    #time.sleep(5)
    
    # 캐시에 부재
    try:
        html = fetch_file("index.html")
        css = fetch_file("index.css")
    except requests.RequestException as e:
        logging.info(f"‼️ SSR 실패: {e}")
        return Response(f"MinIO 연결 실패: {e}", status=503)

    # CSS 인라인 삽입
    html_with_css = html.replace("<!-- CSS_PLACEHOLDER -->", f"<style>{css}</style>")

    # 캐시에 저장(5분=300초)
    set_cache(cache_key, html_with_css, ttl=300)

    duration = time.time() - start
    logging.info(f"✅ SSR 처리 완료 (처리 시간: {duration:.4f}초)")
    
    return Response(html_with_css, mimetype="text/html; charset=utf-8")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
