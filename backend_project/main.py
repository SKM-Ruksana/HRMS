from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas
from fastapi.middleware.cors import CORSMiddleware
 
app = FastAPI(title="HRMS Lite API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
Base.metadata.create_all(bind=engine)
 
# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
# ---------------- Employees ----------------
 
@app.post("/employees")
def add_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Employee).filter(
        models.Employee.employeeId == emp.employeeId
    ).first()
 
    if existing:
        raise HTTPException(status_code=400, detail="Employee already exists")
 
    new_emp = models.Employee(**emp.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return {"message": "Employees added successfully"}
 
 
@app.get("/employees")
def get_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()
 
 
@app.delete("/employees/{employeeId}")
def delete_employee(employeeId: str, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(
        models.Employee.employeeId == employeeId
    ).first()
 
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
 
    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted"}
 
# ---------------- Attendance ----------------
 
@app.post("/attendance")
def mark_attendance(att: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    new_att = models.Attendance(**att.dict())
    db.add(new_att)
    db.commit()
    return {"message": "Attendance marked"}
 
 
@app.get("/attendance/{employeeId}")
def get_attendance(employeeId: str, db: Session = Depends(get_db)):
    return db.query(models.Attendance).filter(
        models.Attendance.employeeId == employeeId
    ).all()
 