from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# Shared properties for an Ick
class IckBase(BaseModel):
    title: str = Field(..., max_length=150)
    description: Optional[str] = Field(None, max_length=300)
    category: str = Field(..., max_length=50)


# Schema for creating an Ick (client input)
class IckCreate(IckBase):
    pass


# Schema for returning an Ick (response)
class Ick(IckBase):
    ick_id: str
    user_id: str
    upvotes: int = 0
    downvotes: int = 0
    created_at: datetime

    class Config:
        from_attributes = True


# Shared properties for a User
class UserBase(BaseModel):
    username: str
    email: str


# Schema for creating a User (client input)
class UserCreate(UserBase):
    password: str
    bio: Optional[str] = None
    avatar_url: Optional[str] = None


# Schema for returning a User (response)
class User(UserBase):
    user_id: str
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


# Shared properties for a Comment
class CommentBase(BaseModel):
    content: str = Field(..., max_length=500)


# Schema for creating a Comment (client input)
class CommentCreate(CommentBase):
    pass


# Schema for returning a Comment (response)
class Comment(CommentBase):
    comment_id: str
    ick_id: str
    user_id: str
    upvotes: int = 0
    downvotes: int = 0
    created_at: datetime

    class Config:
        from_attributes = True
