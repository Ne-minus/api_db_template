## Мои вопросы

**1.** Почему, когда делала ```docker compose up``` вылезала ошибка в db.py с переменной окружения (урла до бдшки)?
```python
os.getenv("POSTGRES_URL") -> None
os.environ["POSTGRES_URL"] -> actual path
```
**Ответ:** это какой-то баг
**Notion:**
**```os.getenv("VAR", default=...)``` vs. ```os.environ[...]```:** первое -- удобно читать, можно избегать KeyError, если переменной нет и ставить какое-то дефолтное рабочее значение; второе -- явная проверка, добавление/изменение/удаление

**2.** Что такое ```orm_mode=True``` в pydantic?

**Ответ:** Флаг, чтобы мы могли вернуть в хэндлере ORM объект: разрешает методу from_orm() брать данные из произвольных атрибутов объекта, а не только из ключей словаря --> когда FastAPI дергает этот метод (автоматом), то мы не упадем с ошибкой.

**По умному:**
Pydantic can read attributes from an object instance to populate its fields, rather than expecting a dictionary-like structure. This is particularly useful when working with ORM objects, as they typically expose data as instance attributes.
