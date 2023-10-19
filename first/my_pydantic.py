from pydantic import BaseModel


class User(BaseModel):
    username: str
    age: int
    email: str
    password: str
