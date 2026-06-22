from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from contextlib import asynccontextmanager

from app.api.doctor import router as doctor_router
from app.api.auth import router as auth_router
from app.api.patient import router as patient_router
from app.api.appointment import router as appointment_router

from app.exceptions.doctor_exception import DoctorNotFoundException
from app.exceptions.patient_exception import PatientNotFoundException
from app.exceptions.appointment_exception import AppointmentNotFoundException

from app.exceptions.auth_exception import (
    InvalidCredentialsException,
    UserAlreadyExistsException,
    UnauthorizedException
)

from app.middleware.logging_middleware import LoggingMiddleware
from app.core.logger import logger

@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info(
        "Application started"
    )

    yield

    logger.info(
        "Application stopped"
    )

app = FastAPI(
    lifespan=lifespan
)

app.include_router(doctor_router)
app.include_router(auth_router)
app.include_router(patient_router)
app.include_router(appointment_router)

app.add_middleware(
    LoggingMiddleware
)

@app.exception_handler(
    DoctorNotFoundException
)
async def doctor_not_found_exception_handler(
    request: Request,
    exc: DoctorNotFoundException
):
    
    return JSONResponse(
        status_code=404,

        content= {
            "detail": (
                f"Doctor with id "
                f"{exc.doctor_id}"
                f"not found"
            )
        }
    )

@app.exception_handler(
    InvalidCredentialsException
)
async def invalid_credentials_exception_handler(
    request: Request,
    exc: InvalidCredentialsException
):
    
    return JSONResponse(
        status_code=401,
        content={
            "detail": "Invalid username or password"
        }
    )


@app.exception_handler(
    UserAlreadyExistsException
)
async def user_already_exists_exception_handler(
    request: Request,
    exc: UserAlreadyExistsException
):

    return JSONResponse(
        status_code= 409,
        content={
            "detail": "Username already exists"
        }
    )


@app.exception_handler(
    UnauthorizedException
)
async def unauthorized_exception_handler(
    request: Request,
    exc: UnauthorizedException
):
    
    return JSONResponse(
        status_code= 403,
        content={
            "detail": "You don't have permission to perform this action"
        }
    )


@app.exception_handler(
    PatientNotFoundException
)
async def patient_not_found_exception_handler(
    request: Request,
    exc: PatientNotFoundException
):
    
    return JSONResponse(
        status_code=404,
        content={
            "detail": "Patient not found"
        }
    )


@app.exception_handler(
    AppointmentNotFoundException
)
async def appointment_not_found_exception_handler(
    request: Request,
    exc: AppointmentNotFoundException
):
    
    return JSONResponse(
        status_code = 404,
        content= {
            "detail": 
            f"Appointment with id {exc.appointment_id} not found"
        }
    )