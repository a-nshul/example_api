from pydantic import BaseModel, EmailStr

class Employee(BaseModel):
    employee_id: str
    name: str
    email: EmailStr
    department: str


class Attendance(BaseModel):
    employee_id: str
    date: str
    status: str
