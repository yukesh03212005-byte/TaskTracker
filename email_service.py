import os
import smtplib
from email.message import EmailMessage

# Read credentials from Streamlit Secrets (Environment Variables)

SENDER_EMAIL = os.environ["SENDER_EMAIL"]
APP_PASSWORD = os.environ["APP_PASSWORD"]
RECEIVER_EMAIL = os.environ["RECEIVER_EMAIL"]


def send_email(tasks):
    """
    Send an email containing all pending tasks.
    """

    if len(tasks) == 0:
        return False

    body = """Hello,

This is an automatic reminder from TaskTrack.

The following tasks are still pending:

"""

    for task in tasks:
        body += f"• {task['title']}\n"

    body += """

Please remind me to complete these tasks.

Regards,
TaskTrack
"""

    message = EmailMessage()

    message["Subject"] = "Task Reminder - Pending Tasks"
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL

    message.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(
                SENDER_EMAIL,
                APP_PASSWORD
            )

            smtp.send_message(message)

        print("Email Sent Successfully")
        return True

    except Exception as e:
        print(f"Email Error: {e}")
        raise