from pydantic import BaseModel


class PasswordCreate(BaseModel):
    service_name: str
    password: str


class PasswordResponse(BaseModel):
    id: int
    service_name: str
    encrypted_password: str
