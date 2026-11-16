
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.patient import Patient
from app.schemas.patient import PatientCreate
from app.schemas.patient import PatientCreate, PatientUpdate,PatientResponse
from fastapi import HTTPException
router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.post("/",response_model=PatientResponse)
async def create_patient(
    patient: PatientCreate,
    db: AsyncSession = Depends(get_db)
):
    new_patient = Patient(**patient.model_dump())

    db.add(new_patient)

    await db.commit()

    await db.refresh(new_patient)

    return new_patient


from sqlalchemy import select


@router.get("/",response_model=list[PatientResponse])
async def get_all_patients(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Patient))

    patients = result.scalars().all()

    return patients


@router.get("/{patient_id}", response_model=PatientResponse)
async def get_patient_by_id(
    patient_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Patient).where(Patient.id == patient_id)
    )

    patient = result.scalar_one_or_none()

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient

@router.put("/{patient_id}",response_model=PatientResponse)
async def update_patient(
    patient_id: int,
    patient_data: PatientUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Patient).where(Patient.id == patient_id)
    )

    patient = result.scalar_one_or_none()

    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    update_data = patient_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(patient, key, value)

    await db.commit()
    await db.refresh(patient)

    return patient



@router.delete("/{patient_id}")
async def delete_patient(
    patient_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Patient).where(Patient.id == patient_id)
    )

    patient = result.scalar_one_or_none()

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    await db.delete(patient)
    await db.commit()

    return {
        "message": "Patient deleted successfully"
    }
