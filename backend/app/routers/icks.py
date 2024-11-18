from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()


@router.post("/icks/", response_model=schemas.Ick)
def create_ick(ick: schemas.IckCreate, db: Session = Depends(database.get_db)):
    user_id = "da6aa77b-dfe6-4893-b7be-879bfbbd9235"  # TODO: Get user_id from token
    return crud.create_ick(db=db, ick=ick, user_id=user_id)


@router.get("/icks/", response_model=list[schemas.Ick])
def read_icks(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_icks(db, skip=skip, limit=limit)
