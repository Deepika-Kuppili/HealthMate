import smtplib
from email.message import EmailMessage

def send_email(subject, content, to_email):
    msg = EmailMessage()
    msg.set_content(content)
    msg["Subject"] = subject
    msg["From"] = "your@email.com"
    msg["To"] = to_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("your@email.com", "your_password")
        server.send_message(msg)
