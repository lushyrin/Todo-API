from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime


# User Schemas
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username (3-50 characters)")
    email: EmailStr = Field(..., description="Valid email address")


class UserCreate(UserBase):
    password: str = Field(..., min_length=6, max_length=100, description="Password (minimum 6 characters)")


class UserResponse(UserBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


# Task Schemas
class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Task title (1-200 characters)")
    description: Optional[str] = Field(None, max_length=1000, description="Task description (max 1000 characters)")
    completed: bool = Field(default=False, description="Task completion status")


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200, description="Task title (1-200 characters)")
    description: Optional[str] = Field(None, max_length=1000, description="Task description (max 1000 characters)")
    completed: Optional[bool] = Field(None, description="Task completion status")


class TaskResponse(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime
    owner_id: int

    model_config = ConfigDict(from_attributes=True)
