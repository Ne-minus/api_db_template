# api_db_template

fastapi
uvicorn
pydantic
pydantic-settings
SQLAlchemy
alembic

# 1. Docker

Делаем приложение в двух контейнерах:
- контейнер api
- контейнер базы данных

Запуск:
```bash
docker-compose up --build
```

## Инструкция установки Docker:
### **Ubuntu**:

https://docs.docker.com/engine/install/ubuntu/

### **Windows**:

> Должна быть поднята WSL2 с Ubuntu
> Проблема в том, что нативного Docker'a для Windows он, он будет работать в любом случае через WSL2
https://docs.docker.com/desktop/setup/install/windows-install/

### **Mac**:

https://docs.docker.com/desktop/setup/install/mac-install/
