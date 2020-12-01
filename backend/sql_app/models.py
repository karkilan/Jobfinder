from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(50))
    job_name = Column(String(50))
    location = Column(String(50))
    salary = Column(Integer)
    job_type = Column(String(50))
    experiance = Column(String(50))
    notes = Column(String(50))

    jobapply = relationship("JobApply", back_populates="owner")

class JobApply(Base):
    __tablename__ = "jobapply"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    dept = Column(String(50))
    email = Column(String(50), unique=True, index=True)
    mobile = Column(Integer)
    college = Column(String(50))
    passing = Column(String(50))
    experiance = Column(Integer)
    notice = Column(String(50))
    owner_id = Column(Integer, ForeignKey("jobs.id"))

    owner = relationship("Job", back_populates="jobapply")
    
    
