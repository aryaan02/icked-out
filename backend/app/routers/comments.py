from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()


@router.post("/comments/", response_model=schemas.Comment)
def create_comment(
    comment: schemas.CommentCreate,
    ick_id: str,
    user_id: str,
    db: Session = Depends(database.get_db),
):
    db_ick = crud.get_ick(db, ick_id=ick_id)
    if not db_ick:
        raise HTTPException(status_code=404, detail="Ick not found")
    return crud.create_comment(db=db, comment=comment, ick_id=ick_id, user_id=user_id)


@router.get("/comments/{ick_id}", response_model=list[schemas.Comment])
def read_comments(ick_id: str, db: Session = Depends(database.get_db)):
    db_ick = crud.get_ick(db, ick_id=ick_id)
    if not db_ick:
        raise HTTPException(status_code=404, detail="Ick not found")
    return crud.get_comments_by_ick(db=db, ick_id=ick_id)
