import smtplib
from email.message import EmailMessage

def send_email(to, subject, body, smtp_server="smtp.gmail.com", port=465):
    msg = EmailMessage()
    msg["From"] = "you@gmail.com"
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)
    
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login("you@gmail.com", "your_password")
        server.send_message(msg)
    
    print(f"Email sent to {to}!")

send_email("boss@example.com", "Daily Report", "Sales: ,234")
