from typing import List, Optional

from sqlalchemy import delete, select

from src.core.db import AsyncSessionLocal
from src.core.models import Employee

# from sqlalchemy.ext.asyncio import AsyncSession


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


async def get_employee_by_name(name: str) -> Optional[Employee]:
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Employee).where(Employee.name == name).limit(1)
        )
        return result.scalar_one_or_none()


async def list_employees() -> List[Employee]:
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Employee))
        return result.scalars().all()


async def delete_employee(id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(delete(Employee).where(Employee.id == id))
        await session.commit()
        return result.rowcount
