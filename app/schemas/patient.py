
from pydantic import BaseModel, EmailStr, Field


class PatientCreate(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=100)
    last_name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=15)
    age: int = Field(..., gt=0, le=120)
    gender: str

class PatientUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    age: int | None = None
    gender: str | None = None

class PatientResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    age: int
    gender: str

    model_config = {
        "from_attributes": True
    }