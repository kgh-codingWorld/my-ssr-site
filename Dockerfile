FROM python:3.10-slim

WORKDIR /app

COPY . /app 

RUN pip install flask requests redis python-dotenv

CMD ["python", "-m", "server.app"]