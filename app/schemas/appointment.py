from pydantic import BaseModel, Field
from datetime import date, time


class AppointmentCreate(BaseModel):

    patient_id: int = Field(..., gt=0)

    doctor_id: int = Field(..., gt=0)

    appointment_date: date

    appointment_time: time

    reason: str = Field(..., min_length=3, max_length=255)


class AppointmentResponse(BaseModel):

    id: int
    patient_id: int
    doctor_id: int
    appointment_date: date
    appointment_time: time
    reason: str
    status: str

    model_config = {
        "from_attributes": True
    }


class AppointmentStatusUpdate(BaseModel):
    status: str = Field(
        ...,
        pattern="^(Scheduled|Completed|Cancelled)$"
    )