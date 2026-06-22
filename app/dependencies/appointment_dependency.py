from app.repositories.appointment_repository import AppointmentRepository
from app.services.appointment_service import AppointmentService

def get_appointment_service() -> AppointmentService:

    appointment_repository = AppointmentRepository()

    return AppointmentService(appointment_repository)