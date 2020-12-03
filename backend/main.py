from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

# Dependency
def get_db(request: Request):
    return request.state.db

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/jobs/", response_model=schemas.Item)
def create_jobs(job: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_job(db, job)
    

@app.get("/jobs/", response_model=List[schemas.Item])
def get_jobs(db: Session = Depends(get_db)):
    return crud.get_jobs(db)

# @app.delete("/jobs/", response_model=schemas.Item)
# def delete_all_jobs(job: schemas.ItemDelete, db: Session = Depends(get_db)):
#     return crud.delete_jobs(db, job)

@app.delete("/jobs/{job_id}", response_model=schemas.Item)
def delete_job_id(job_id: int, db: Session = Depends(get_db)):
    return crud.delete_jobs_id(db, job_id)

@app.get("/job/{job_id}", response_model=schemas.Item)
def get_job_id( job_id: int, db: Session = Depends(get_db)):
    items = crud.get_job_id(db, job_id)
    return items

@app.put("/job/{job_id}", response_model=schemas.Item)
def update_by_id(job_id: int, job: schemas.ItemUpdate, db: Session = Depends(get_db)):
    items = crud.update(db, job_id, job)
    return items

@app.post("/jobs/{job_id}/apply/", response_model=schemas.Job)
def create_candidate(job_id: int, item: schemas.JobCreate, db: Session = Depends(get_db)):
    item = crud.create_candidate(db, item, job_id)
    return item