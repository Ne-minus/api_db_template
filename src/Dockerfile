FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY /src ./src

RUN pip install -r requirements.txt

CMD ["python", "/app/src/main.py"]
