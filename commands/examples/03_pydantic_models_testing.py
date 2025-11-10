from datetime import datetime
from pydantic import BaseModel


class EmailRecord(BaseModel):
    to: str
    subject: str
    body: str
    sent_at: datetime


class UserData(BaseModel):
    name: str
    age: int
    id: int | None = None

