FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY . .

RUN pip install -r requirements.txt

#CMD ["python", "/app/src/main.py"]
CMD ["python", "-m", "src.main"]
