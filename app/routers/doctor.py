from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorResponse


router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"]
)


# Create Doctor
@router.post("/", response_model=DoctorResponse)
async def create_doctor(
    doctor: DoctorCreate,
    db: AsyncSession = Depends(get_db)
):
    new_doctor = Doctor(**doctor.model_dump())

    db.add(new_doctor)
    await db.commit()
    await db.refresh(new_doctor)

    return new_doctor

# Get All Doctors
@router.get("/", response_model=list[DoctorResponse])
async def get_all_doctors(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Doctor))

    doctors = result.scalars().all()

    return doctors

# Get Doctor by ID
@router.get("/{doctor_id}", response_model=DoctorResponse)
async def get_doctor_by_id(
    doctor_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Doctor).where(Doctor.id == doctor_id)
    )

    doctor = result.scalar_one_or_none()

    if doctor is None:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    return doctor

# Update Doctor
@router.put("/{doctor_id}", response_model=DoctorResponse)
async def update_doctor(
    doctor_id: int,
    doctor_data: DoctorCreate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Doctor).where(Doctor.id == doctor_id)
    )

    doctor = result.scalar_one_or_none()

    if doctor is None:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    update_data = doctor_data.model_dump()

    for key, value in update_data.items():
        setattr(doctor, key, value)

    await db.commit()
    await db.refresh(doctor)

    return doctor

# Delete Doctor
@router.delete("/{doctor_id}")
async def delete_doctor(
    doctor_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Doctor).where(Doctor.id == doctor_id)
    )

    doctor = result.scalar_one_or_none()

    if doctor is None:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    await db.delete(doctor)
    await db.commit()

    return {
        "message": "Doctor deleted successfully"
    }