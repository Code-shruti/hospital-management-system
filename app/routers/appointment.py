from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models.appointment import Appointment
from app.models.patient import Patient
from app.models.doctor import Doctor
from app.schemas.appointment import AppointmentCreate, AppointmentResponse, AppointmentStatusUpdate

router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)


# Book Appointment
@router.post("/", response_model=AppointmentResponse)
async def create_appointment(
    appointment: AppointmentCreate,
    db: AsyncSession = Depends(get_db)
):
    # Check patient exists
    patient_result = await db.execute(
        select(Patient).where(Patient.id == appointment.patient_id)
    )
    patient = patient_result.scalar_one_or_none()

    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    # Check doctor exists
    doctor_result = await db.execute(
        select(Doctor).where(Doctor.id == appointment.doctor_id)
    )
    doctor = doctor_result.scalar_one_or_none()

    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")

    new_appointment = Appointment(**appointment.model_dump())

    db.add(new_appointment)
    await db.commit()
    await db.refresh(new_appointment)

    return new_appointment

# Get All Appointments
@router.get("/", response_model=list[AppointmentResponse])
async def get_all_appointments(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Appointment))

    appointments = result.scalars().all()

    return appointments


# Get Appointment by ID
@router.get("/{appointment_id}", response_model=AppointmentResponse)
async def get_appointment_by_id(
    appointment_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Appointment).where(Appointment.id == appointment_id)
    )

    appointment = result.scalar_one_or_none()

    if appointment is None:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    return appointment


# Update Appointment
@router.put("/{appointment_id}", response_model=AppointmentResponse)
async def update_appointment(
    appointment_id: int,
    appointment_data: AppointmentCreate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Appointment).where(Appointment.id == appointment_id)
    )

    appointment = result.scalar_one_or_none()

    if appointment is None:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    # Check patient exists
    patient_result = await db.execute(
        select(Patient).where(
            Patient.id == appointment_data.patient_id
        )
    )
    if patient_result.scalar_one_or_none() is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    # Check doctor exists
    doctor_result = await db.execute(
        select(Doctor).where(
            Doctor.id == appointment_data.doctor_id
        )
    )
    if doctor_result.scalar_one_or_none() is None:
        raise HTTPException(status_code=404, detail="Doctor not found")

    update_data = appointment_data.model_dump()

    for key, value in update_data.items():
        setattr(appointment, key, value)

    await db.commit()
    await db.refresh(appointment)

    return appointment


# Delete Appointment
@router.delete("/{appointment_id}")
async def delete_appointment(
    appointment_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Appointment).where(Appointment.id == appointment_id)
    )

    appointment = result.scalar_one_or_none()

    if appointment is None:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    await db.delete(appointment)
    await db.commit()

    return {
        "message": "Appointment cancelled successfully"
    }

# Cancel Appointment
@router.patch("/{appointment_id}/status", response_model=AppointmentResponse)
async def update_appointment_status(
    appointment_id: int,
    status_data: AppointmentStatusUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Appointment).where(Appointment.id == appointment_id)
    )

    appointment = result.scalar_one_or_none()

    if appointment is None:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    appointment.status = status_data.status

    await db.commit()
    await db.refresh(appointment)

    return appointment