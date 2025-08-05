from fastapi import APIRouter
from typing_extensions import Any

from src.services.DBService import create_employee

router = APIRouter()


@router.post("/employee")
async def employee(data: dict[Any, Any]):
    employee = await create_employee(data)
    return employee
