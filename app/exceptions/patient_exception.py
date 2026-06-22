class PatientNotFoundException(Exception):
    
    def __init__(
        self,
        patient_id: int
    ):
        
        self.patient_id = patient_id