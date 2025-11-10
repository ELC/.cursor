from pydantic import BaseModel


class ValidatedData(BaseModel):
    email: str
    status: str

