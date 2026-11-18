
from fastapi import FastAPI
from sqlalchemy import text
from app.models.patient import Patient
from app.models.doctor import Doctor
from app.models.appointment import Appointment
from app.database import engine
from contextlib import asynccontextmanager
from app.database import Base
from app.routers.patient import router as patient_router
from app.routers.doctor import router as doctor_router
from app.routers.appointment import router as appointment_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    yield

app = FastAPI(
    title="Hospital Management System",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(patient_router)
app.include_router(doctor_router)
app.include_router(appointment_router)

@app.get("/")
async def home():
    return {
        "message": "Welcome to Hospital Management System"
    }


@app.get("/test-db")
async def test_database():

    async with engine.connect() as connection:
        result = await connection.execute(text("SELECT 1"))

        return {
            "message": "PostgreSQL connected successfully",
            "result": result.scalar()
        }
