from pydantic import BaseModel, ConfigDict, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "user"

class UserUpdate(BaseModel):
    name: str | None = None
    is_active: bool | None = None

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None
    role: str | None = None