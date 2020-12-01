from pydantic import BaseModel
from typing import List

class JobBase(BaseModel):
    name: str
    dept: str
    email: str
    mobile: int
    college: str
    passing: str
    experiance: int
    notice: str

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
    

class ItemBase(BaseModel):
    job_name: str
    company_name: str
    location: str
    job_type:str
    salary: int
    experiance: str
    notes: str

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

# class ItemDelete(ItemBase):
#     id: int

class Item(ItemBase):
    id: int
    jobapply: List[Job] = []

    class Config:
        orm_mode = True
