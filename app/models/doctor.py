from sqlalchemy import Column, Integer, String
from app.database import Base


class Doctor(Base):

    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(100), nullable=False)

    last_name = Column(String(100), nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    phone = Column(String(15), nullable=False)

    specialization = Column(String(100), nullable=False)

    experience_years = Column(Integer, nullable=False)