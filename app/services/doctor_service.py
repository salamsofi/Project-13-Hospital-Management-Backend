import json

from sqlalchemy.orm import Session

from app.core.logger import logger
from app.core.redis import redis_client
from app.models.doctor import Doctor

from app.repositories.doctor_repository import DoctorRepository
from app.schemas.doctor_schema import DoctorCreate, DoctorUpdate
from app.exceptions.doctor_exception import DoctorNotFoundException

class DoctorService:

    def __init__(
        self, 
        doctor_repository: DoctorRepository
    ):
        
        self.doctor_repository = doctor_repository

    
    def create_doctor(
        self,
        db: Session,
        doctor_data: DoctorCreate
    ) -> Doctor:

        logger.info(
            f"Creating doctor {doctor_data.name}"
        )

        doctor = self.doctor_repository.create(
            db, 
            doctor_data
        )

        redis_client.delete(
            "all_doctors"
        )

        return doctor
    

    def get_all_doctors(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 10,
        search: str | None = None,
        sort_by: str = "id",
        sort_order: str = "asc"
    ) -> list:
        
        cache_key = "all_doctors"

        cached_data = redis_client.get(
            cache_key
        )

        if cached_data:

            logger.info(
                "Returning doctors from Redis cache"
            )

            return json.loads(
                cached_data
            )

        logger.info(
            f"Fetching doctors from PostgreSQL"
        )
        
        doctors = self.doctor_repository.get_all(
            db,
            skip,
            limit,
            search,
            sort_by,
            sort_order
        )

        doctors_data = [
            {
                "id": doctor.id,
                "name": doctor.name,
                "specialization": doctor.specialization
            }
            for doctor in doctors
        ]

        redis_client.set(
            cache_key,
            json.dumps(
                doctors_data
            ),
            ex=300
        )

        return doctors_data
    

    def get_doctor_by_id(
        self,
        db: Session,
        doctor_id: int
    ) -> Doctor | dict:

        cache_key = f"doctor: {doctor_id}"

        cached_data = redis_client.get(
            cache_key
        )

        if cached_data:

            logger.info(
                f"Returning doctor {doctor_id} from Redis cache"
            )

            return json.load(
                cached_data
            )

        logger.info(
            f"Fetching doctor {doctor_id} from PostgreSQL"
        )

        doctor = self.doctor_repository.get_by_id(
            db,
            doctor_id
        )

        if doctor is None:
            logger.warning(
                f"Doctor with id {doctor_id} not found"
            )

            raise DoctorNotFoundException(
                doctor_id
            )

        doctor_data = {
            "id": doctor.id,
            "name": doctor.name,
            "specialization": doctor.specialization
        }

        redis_client.set(
            cache_key,
            json.dumps(
                doctor_data
            ),
            ex=300
        )

        return doctor_data

    def update_doctor(
        self,
        db: Session,
        doctor_id: int,
        doctor_data: DoctorUpdate
    ) -> Doctor:
        
        doctor = self.doctor_repository.get_by_id(
            db,
            doctor_id
        )

        if doctor is None:
            logger.warning(
                f"Doctor with id {doctor_id} not found"
            )

            raise DoctorNotFoundException(
                doctor_id
            )

        logger.info(
            f"Updating doctor with id {doctor_id}"
        )

        updated_doctor = self.doctor_repository.update(
            db,
            doctor,
            doctor_data
        )

        redis_client.delete(
            "all_doctors"
        )

        redis_client.delete(
            f"doctor: {doctor_id}"
        )

        return updated_doctor


    def delete_doctor(
        self,
        db: Session,
        doctor_id: int
    ) -> None:
        
        doctor = self.doctor_repository.get_by_id(
            db,
            doctor_id
        )

        if doctor is None:
            logger.warning(
                f"Doctor with id {doctor_id} not found"
            )

            raise DoctorNotFoundException(
                doctor_id
            )
        
        logger.info(
            f"Deleting doctor with id {doctor_id}"
        )

        self.doctor_repository.delete(
            db,
            doctor
        )

        redis_client.delete(
            "all_doctors"
        )

        redis_client.delete(
            f"doctor: {doctor_id}"
        )