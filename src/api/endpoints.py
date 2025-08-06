from fastapi import APIRouter, HTTPException, Response

from src.schemas.employee import EmployeeCreate, EmployeeRead
from src.services.DBService import (
    create_employee,
    delete_employee,
    get_employee_by_name,
)

router = APIRouter()


@router.post("/employee", response_model=EmployeeRead, status_code=201)
async def create_employee_ep(payload: EmployeeCreate):
    employee = await create_employee(payload.model_dump())
    return employee


@router.get("/employee/{name}", response_model=EmployeeRead)
async def get_employee_ep(name: str):
    emp = await get_employee_by_name(name)
    if not emp:
        raise HTTPException(status_code=404, detail="Not found")
    return emp


@router.delete("/employee/{id}", status_code=204)
async def delete_employee_ep(id: int):
    rows = await delete_employee(id)
    if not rows:
        raise HTTPException(status_code=404, detail="Not found")
    return Response(status_code=204)
