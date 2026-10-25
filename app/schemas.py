from pydantic import BaseModel, ConfigDict, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserUpdate(BaseModel):
    name: str | None = None
    is_active: bool | None = None

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool

    model_config = ConfigDict(from_attributes=True)