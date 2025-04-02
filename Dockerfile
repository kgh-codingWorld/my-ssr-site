FROM python:3.10-slim

WORKDIR /app

COPY . /app 

RUN pip install flask requests python-dotenv psycopg2-binary

CMD ["python", "-m", "server.app"]