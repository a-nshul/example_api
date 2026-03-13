from fastapi import APIRouter, HTTPException
from database import db  # relative import
from models import Employee

router = APIRouter()


@router.get("/employees")
def get_employees():
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()
    finally:
        cursor.close()
    return employees


@router.post("/employees")
def add_employee(emp: Employee):
    cursor = db.cursor()
    try:
        cursor.execute("SELECT * FROM employees WHERE employee_id=%s", (emp.employee_id,))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="Employee already exists")

        cursor.execute(
            "INSERT INTO employees (employee_id, name, email, department) VALUES (%s, %s, %s, %s)",
            (emp.employee_id, emp.name, emp.email, emp.department)
        )
        db.commit()
    finally:
        cursor.close()
    return {"message": "Employee added"}


@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: str):
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM employees WHERE employee_id=%s", (employee_id,))
        db.commit()
    finally:
        cursor.close()
    return {"message": "Employee deleted"}
