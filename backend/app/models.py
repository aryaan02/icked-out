from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Text, TIMESTAMP, func
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    bio = Column(Text, nullable=True)
    avatar_url = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, default=func.now())

    icks = relationship("Ick", back_populates="author")

class Ick(Base):
    __tablename__ = "icks"

    ick_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String, nullable=False)
    upvotes = Column(Integer, default=0)
    downvotes = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, default=func.now())

    author = relationship("User", back_populates="icks")
    comments = relationship("Comment", back_populates="ick")

class Comment(Base):
    __tablename__ = "comments"

    comment_id = Column(String, primary_key=True)
    ick_id = Column(String, ForeignKey("icks.ick_id"), nullable=False)
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False)
    content = Column(Text, nullable=False)
    upvotes = Column(Integer, default=0)
    downvotes = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, default=func.now())

    ick = relationship("Ick", back_populates="comments")