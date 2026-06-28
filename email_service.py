import smtplib
from email.message import EmailMessage

from config import (
    SENDER_EMAIL,
    APP_PASSWORD,
    RECEIVER_EMAIL
)


def send_email(tasks):

    print("Sender:", SENDER_EMAIL)
    print("Receiver:", RECEIVER_EMAIL)
    print("Password Length:", len(APP_PASSWORD))

    body = "Pending Tasks\n\n"

    for task in tasks:
        body += f"- {task['title']}\n"

    msg = EmailMessage()

    msg["Subject"] = "Task Reminder"

    msg["From"] = SENDER_EMAIL

    msg["To"] = RECEIVER_EMAIL

    msg.set_content(body)

    try:

        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        smtp.login(SENDER_EMAIL, APP_PASSWORD)

        smtp.send_message(msg)

        smtp.quit()

        print("EMAIL SENT")

    except Exception as e:

        print(e)

        raise