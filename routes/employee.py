from fastapi import APIRouter, HTTPException
from database import cursor, db
from models import Employee

router = APIRouter()


@router.get("/employees")
def get_employees():

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    return employees


@router.post("/employees")
def add_employee(emp: Employee):

    cursor.execute(
        "SELECT * FROM employees WHERE employee_id=%s",
        (emp.employee_id,)
    )

    existing = cursor.fetchone()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Employee already exists"
        )

    cursor.execute(
        "INSERT INTO employees VALUES (%s,%s,%s,%s)",
        (
            emp.employee_id,
            emp.name,
            emp.email,
            emp.department
        )
    )

    db.commit()

    return {"message": "Employee added"}


@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: str):

    cursor.execute(
        "DELETE FROM employees WHERE employee_id=%s",
        (employee_id,)
    )

    db.commit()

    return {"message": "Employee deleted"}
