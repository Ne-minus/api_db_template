from src.core.db import AsyncSessionLocal
from src.core.models import Employee


async def create_employee(data: dict):
    # {
    #     "name": "Ivan",
    #     "age": 22,
    #     "gender": "Male",
    # }
    db_employee = Employee(**data)
    async with AsyncSessionLocal() as session:
        session.add(db_employee)
        await session.commit()  # фиксируем состояние базы, сохраняем изменения
        await session.refresh(db_employee)  # обновляем db_employee
        await session.close()  # закрываем сессию
        return db_employee
