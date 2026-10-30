from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Student(BaseModel):
    id : Optional[int] = None 
    name: str
    course: str
    marks: float