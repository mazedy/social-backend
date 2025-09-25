from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


# ---------- User Schemas ----------
class UserCreate(BaseModel):
    username: str
    email: EmailStr


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None


class UserOut(BaseModel):
    uid: str
    username: str
    email: EmailStr


# ---------- Post Schemas ----------
class PostCreate(BaseModel):
    content: str


class PostOut(BaseModel):
    uid: str
    content: str
    created_at: datetime


# ---------- Follow Schemas ----------
class FollowOut(BaseModel):
    uid: str
    username: str
    email: EmailStr
