from fastapi import APIRouter
from database import cursor, db
from models import Attendance

router = APIRouter()


@router.post("/attendance")
def mark_attendance(att: Attendance):

    cursor.execute(
        "INSERT INTO attendance (employee_id,date,status) VALUES (%s,%s,%s)",
        (
            att.employee_id,
            att.date,
            att.status
        )
    )

    db.commit()

    return {"message": "Attendance saved"}


@router.get("/attendance/{employee_id}")
def get_attendance(employee_id: str):

    cursor.execute(
        "SELECT * FROM attendance WHERE employee_id=%s",
        (employee_id,)
    )

    records = cursor.fetchall()

    return records
