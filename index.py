import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = "smtp-mail.outlook.com"

current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()

envars = current_dir / ".env"
load_dotenv(envars)

sender_email = os.getenv("email")
password_email = os.getenv("password")

def send_email(subject, receiver_email, name, due_date, invoice_no, amount):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Coding is fun corp.", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Hi {name},

        I hope you are well.

        This is a reminder that you owe {amount}. Your payment is due by {due_date}, as indicated on invoice number {invoice_no}.

        Please ensure that the payment is made promptly.

        Best regards,
        Coding is fun corp.
        """
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.send_message(msg)

if __name__ == "__main__":
    send_email(
        subject="Payment Reminder",
        name="John Doe",
        receiver_email="dbalogun2023@gmail.com",
        due_date="11, Aug 2022",
        invoice_no="INV-2022",
        amount="$5",
    )
