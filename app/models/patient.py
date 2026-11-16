
from sqlalchemy import Column, Integer, String
from app.database import Base


class Patient(Base):

    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(100), nullable=False)

    last_name = Column(String(100), nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    phone = Column(String(15), nullable=False)

    age = Column(Integer, nullable=False)

    gender = Column(String(10), nullable=False)
