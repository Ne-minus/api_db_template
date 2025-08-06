from pydantic import BaseModel


# то, что приходит от клиента (POST /employee)
class EmployeeCreate(BaseModel):
    name: str
    age: int
    gender: str


# то, что мы отдаём наружу (GET, POST-response)
class EmployeeRead(EmployeeCreate):
    id: int

    class Config:
        orm_mode = True
