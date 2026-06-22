class AppointmentNotFoundException(Exception):

    def __init__(
        self,
        appointment_id: int
    ):
        
        self.appointment_id = appointment_id