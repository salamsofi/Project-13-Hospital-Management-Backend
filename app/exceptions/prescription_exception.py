class PrescriptionNotFoundException(Exception):

    def __init__(
        self,
        prescription_id: int
    ):
        
        self.prescription_id = prescription_id