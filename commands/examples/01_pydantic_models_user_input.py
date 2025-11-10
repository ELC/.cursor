from pydantic import BaseModel, EmailStr


class UserInput(BaseModel):
    email: EmailStr
    name: str


class UserInvalidInput(BaseModel):
    email: str
    name: str

