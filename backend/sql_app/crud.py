from . import models, schemas
from sqlalchemy.orm import Session

def get_job_id(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()

def update(db: Session, job_id: int, job: schemas.ItemUpdate):
    db_update = db.query(models.Job).filter(models.Job.id == job_id).update({
        models.Job.company_name : job.company_name,
        models.Job.job_name : job.job_name,
        models.Job.location : job.location,
        models.Job.salary : job.salary,
        models.Job.job_type : job.job_type,
        models.Job.experiance : job.experiance,
        models.Job.notes : job.notes
        })
    db.commit()
    db.refresh(db_update)
    return db_update

def get_jobs(db: Session):
    return db.query(models.Job).all()

# def delete_jobs(db: Session, job: schemas.ItemDelete):
#     db_item = db.query(models.Job).filter(models.Job.id == job).delete()
#     db.commit()
#     return db_item

def delete_jobs_id(db: Session, job_id:int):
    db_item = db.query(models.Job).filter(models.Job.id == job_id).delete()
    db.commit()
    db.refresh(db_item)
    return db_item

def create_job(db: Session, job: schemas.ItemCreate):
    db_item = models.Job(**job.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_candidate(db: Session, item: schemas.JobCreate, job_id: int):
    db_item = models.JobApply(**item.dict(), owner_id=job_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
