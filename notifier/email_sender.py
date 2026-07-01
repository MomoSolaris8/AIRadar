import os
import smtplib
from email.message import EmailMessage
import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()


def send_email(subject, body):
    email_host = os.environ['EMAIL_HOST']
    email_port = int(os.environ.get('EMAIL_PORT', '587'))
    email_username = os.environ['EMAIL_USERNAME']
    email_password = os.environ['EMAIL_PASSWORD']
    email_to = os.environ['EMAIL_TO']

    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = email_username
    message['To'] = email_to
    message.set_content(body)

    with smtplib.SMTP(email_host, email_port) as smtp:
        smtp.starttls()
        smtp.login(email_username, email_password)
        smtp.send_message(message)
