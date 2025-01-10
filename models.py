from typing import  Optional
from pydantic import BaseModel
from uuid import  UUID,uuid4
from enum import  Enum

class Gender(str,Enum):
    male = 'male'
    female = 'female'

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    age: int
    gender: Gender