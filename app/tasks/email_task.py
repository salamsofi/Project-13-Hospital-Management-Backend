from app.core.logger import logger

def send_welcome_email(
    email: str
):
    
    logger.info(
        f"Sending email to {email}"
    )

    print(
        f"Welcome email sent to {email}"
    )