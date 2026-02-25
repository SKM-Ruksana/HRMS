from sqlalchemy import Column, Integer, String, Date
from database import Base
 
class Employee(Base):
    __tablename__ = "employees"
 
    id = Column(Integer, primary_key=True, index=True)
    employeeId = Column(String, unique=True, index=True)
    fullName = Column(String)
    email = Column(String, unique=True)
    department = Column(String)
 
 
class Attendance(Base):
    __tablename__ = "attendance"
 
    id = Column(Integer, primary_key=True, index=True)
    employeeId = Column(String)
    date = Column(Date)
    status = Column(String)
 