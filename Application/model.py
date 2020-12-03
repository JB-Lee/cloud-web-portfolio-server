from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    password: str
    name: str
    email: Optional[str] = None


class Stock(BaseModel):
    stock_id: str
    stock_name: str
