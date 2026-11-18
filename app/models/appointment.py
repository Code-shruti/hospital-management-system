from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from app.database import Base


class Appointment(Base):

    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)

    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)

    appointment_date = Column(Date, nullable=False)

    appointment_time = Column(Time, nullable=False)

    reason = Column(String(255), nullable=False)

    status = Column(String(20), default="Scheduled")