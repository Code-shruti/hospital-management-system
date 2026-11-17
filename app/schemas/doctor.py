from pydantic import BaseModel, EmailStr, Field


class DoctorCreate(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=100)
    last_name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=15)
    specialization: str
    experience_years: int = Field(..., ge=0)


class DoctorResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    specialization: str
    experience_years: int

    model_config = {
        "from_attributes": True
    }