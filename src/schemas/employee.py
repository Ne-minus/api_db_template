from pydantic import BaseModel


# то, что приходит от клиента (POST /employee)
class EmployeeCreate(BaseModel):
    name: str
    age: int
    gender: str


# то, что мы отдаём наружу (GET, POST-response)
class EmployeeRead(EmployeeCreate):
    id: int

    # чтобы мы могли вернуть в хэндлере ORM объект: разрешает методу from_orm() брать данные из произвольных атрибутов
    # объекта, а не только из ключей словаря -> когда FastAPI дергает этот метод (автоматом), то мы не упадем с ошибкой.
    class Config:
        orm_mode = True
