FROM python:3.13-slim AS base

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


FROM base AS prod

COPY . .
CMD ["python", "-m", "src.main"]
