
# 🏥 Hospital Management System

A Hospital Management System backend developed using Python, FastAPI, SQLAlchemy, and PostgreSQL. This project provides REST APIs to manage patients, doctors, and appointments efficiently.

## 🚀 Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- AsyncPG
- Uvicorn
- Git & GitHub

## ✨ Features

### 👤 Patient Management
- Register new patients
- View all patients
- Get patient details by ID
- Update patient information
- Delete patient records

### 👨‍⚕️ Doctor Management
- Register new doctors
- View all doctors
- Get doctor details by ID
- Update doctor information
- Delete doctor records

### 📅 Appointment Management
- Book appointments
- View all appointments
- Get appointment details by ID
- Update appointment details
- Delete appointments
- Update appointment status
- Manage Scheduled, Completed, and Cancelled appointments

## 📂 Project Structure

```text
hospital_management/
│
├── app/
│   ├── core/
│   │   └── config.py
│   │
│   ├── models/
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   └── appointment.py
│   │
│   ├── schemas/
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   └── appointment.py
│   │
│   ├── routers/
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   └── appointment.py
│   │
│   ├── database.py
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Code-shruti/hospital-management-system.git
```

### 2. Navigate to Project

```bash
cd hospital-management-system
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Database

Create a PostgreSQL database named `hospital_db`.

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+asyncpg://postgres:YOUR_PASSWORD@localhost:5432/hospital_db
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

### 7. Run the Application

```bash
python -m uvicorn app.main:app --reload
```

## 📖 API Documentation

Once the application is running, access the interactive API documentation:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## 🔗 API Endpoints

| Module | Method | Endpoint | Description |
|---|---|---|---|
| Patients | POST | `/patients/` | Create patient |
| Patients | GET | `/patients/` | Get all patients |
| Patients | GET | `/patients/{patient_id}` | Get patient by ID |
| Patients | PUT | `/patients/{patient_id}` | Update patient |
| Patients | DELETE | `/patients/{patient_id}` | Delete patient |
| Doctors | POST | `/doctors/` | Create doctor |
| Doctors | GET | `/doctors/` | Get all doctors |
| Doctors | GET | `/doctors/{doctor_id}` | Get doctor by ID |
| Doctors | PUT | `/doctors/{doctor_id}` | Update doctor |
| Doctors | DELETE | `/doctors/{doctor_id}` | Delete doctor |
| Appointments | POST | `/appointments/` | Book appointment |
| Appointments | GET | `/appointments/` | Get all appointments |
| Appointments | GET | `/appointments/{appointment_id}` | Get appointment |
| Appointments | PUT | `/appointments/{appointment_id}` | Update appointment |
| Appointments | DELETE | `/appointments/{appointment_id}` | Delete appointment |
| Appointments | PATCH | `/appointments/{appointment_id}/status` | Update appointment status |

## 🔒 Security

- Environment variables for database configuration.
- `.env` excluded from Git using `.gitignore`.
- Request validation using Pydantic.

## 👩‍💻 Developer

**Shruti Andhale**

- GitHub: [Code-shruti](https://github.com/Code-shruti)

## 📌 Project Status

Currently implemented:
- Patient Management
- Doctor Management
- Appointment Management
- Appointment Status Management

More features will be added as the project develops.

---

⭐ Thank you for visiting this repository!
