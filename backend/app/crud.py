import uuid
from sqlalchemy.orm import Session
from app import models, schemas
from sqlalchemy.orm import Session


def create_ick(db: Session, ick: schemas.IckCreate, user_id: str):
    db_ick = models.Ick(
        ick_id=str(uuid.uuid4()),
        user_id=user_id,
        title=ick.title,
        description=ick.description,
        category=ick.category,
    )
    db.add(db_ick)
    db.commit()
    db.refresh(db_ick)
    return db_ick


def get_icks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Ick).offset(skip).limit(limit).all()


def get_ick(db: Session, ick_id: str):
    return db.query(models.Ick).filter(models.Ick.ick_id == ick_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        user_id=str(uuid.uuid4()),
        username=user.username,
        email=user.email,
        password_hash=hashed_password,
        bio=user.bio,
        avatar_url=user.avatar_url,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).all()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_comment(
    db: Session, comment: schemas.CommentCreate, ick_id: str, user_id: str
):
    db_comment = models.Comment(
        comment_id=str(uuid.uuid4()),
        ick_id=ick_id,
        user_id=user_id,
        content=comment.content,
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comments_by_ick(db: Session, ick_id: str):
    return db.query(models.Comment).filter(models.Comment.ick_id == ick_id).all()
