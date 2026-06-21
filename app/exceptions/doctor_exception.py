class DoctorNotFoundException(Exception):

    def __init__(self, doctor_id: int):

        self.doctor_id = doctor_id

