# 🏥 Hospital Management System API

A production-inspired backend REST API built using **FastAPI** following clean architecture and industry-standard backend development practices. The project demonstrates authentication, authorization, layered architecture, dependency injection, database migrations, testing, caching, logging, and background task handling.

---

## 🚀 Features

* JWT Authentication
* Role-Based Access Control (RBAC)
* CRUD APIs for Doctors
* CRUD APIs for Patients
* CRUD APIs for Appointments
* CRUD APIs for Prescriptions
* PostgreSQL Database
* SQLAlchemy ORM
* Alembic Database Migrations
* Repository-Service Architecture
* Dependency Injection
* Background Tasks
* Request Logging Middleware
* Custom Exception Handling
* Pydantic Validation
* RESTful API Design
* Automated API Documentation (Swagger UI)
* Unit Testing using Pytest
* Redis Integration (Caching)

---

# 🏗️ Project Architecture

```
Client
   │
   ▼
FastAPI Router
   │
   ▼
Service Layer
   │
   ▼
Repository Layer
   │
   ▼
PostgreSQL Database
```

The project follows a layered architecture where each layer has a single responsibility.

---

# 📁 Project Structure

```
app/
│
├── api/
├── auth/
├── core/
├── db/
├── dependencies/
├── enums/
├── exceptions/
├── middleware/
├── models/
├── repositories/
├── schemas/
├── services/
├── tasks/
├── utils/
│
├── main.py
│
tests/
│
alembic/
│
requirements.txt
README.md
```

---

# 🛠️ Tech Stack

### Backend

* Python 3.13
* FastAPI
* SQLAlchemy ORM
* PostgreSQL
* Alembic
* Pydantic v2

### Authentication

* JWT Authentication
* OAuth2 Password Bearer
* Password Hashing (Passlib + Bcrypt)

### Database

* PostgreSQL
* SQLAlchemy ORM
* Alembic Migrations

### Caching

* Redis

### Testing

* Pytest
* FastAPI TestClient

### Other Tools

* Background Tasks
* Logging Middleware
* Dependency Injection
* Git & GitHub

---

# 📚 API Modules

## Authentication

* Register User
* Login User (JWT)

## Doctors

* Create Doctor
* Get All Doctors
* Get Doctor by ID
* Update Doctor
* Delete Doctor

## Patients

* Create Patient
* Get All Patients
* Get Patient by ID
* Update Patient
* Delete Patient

## Appointments

* Create Appointment
* Get All Appointments
* Get Appointment by ID
* Update Appointment
* Delete Appointment

## Prescriptions

* Create Prescription
* Get All Prescriptions
* Get Prescription by ID
* Update Prescription
* Delete Prescription

---

# 🔐 Authentication

The API uses JWT-based authentication.

After login, include the access token in every protected request:

```
Authorization: Bearer <your_access_token>
```

---

# 👮 Role-Based Access Control (RBAC)

Supported roles:

* Admin
* Doctor
* Receptionist

Protected endpoints enforce role-based authorization using dependency injection.

---

# 🧪 Testing

Unit tests were written using **Pytest** for:

* Authentication
* Doctors
* Patients
* Appointments
* Prescriptions

Run all tests:

```bash
pytest
```

---

# 📖 Interactive API Documentation

Once the server is running:

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# 🚀 Running the Project

## Clone Repository

```bash
git clone https://github.com/salamsofi/Pproject-13-Hospital-Management-Backend
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:<password>@localhost:5432/hospital_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REDIS_HOST=localhost
REDIS_PORT=6379
```

## Run Alembic Migrations

```bash
alembic upgrade head
```

## Start the Server

```bash
uvicorn app.main:app --reload
```

---

# 🎯 Learning Outcomes

This project helped strengthen practical backend engineering skills in:

* Building scalable REST APIs
* Layered software architecture
* Authentication & Authorization
* Database design and relationships
* SQLAlchemy ORM
* Alembic migrations
* Dependency Injection
* Exception Handling
* Middleware
* Background Tasks
* Unit Testing
* API Documentation
* Redis Caching
* Production-oriented FastAPI development

---

# 📌 Future Improvements

* Docker Containerization
* GitHub Actions CI/CD
* Refresh Tokens
* Rate Limiting
* API Versioning
* Monitoring & Observability
* Async Database Support
* Cloud Deployment (AWS/Azure/GCP)

---

# 📄 License

This project is intended for learning and portfolio purposes.
