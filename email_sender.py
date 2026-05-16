import smtplib
from email.message import EmailMessage

def send_email(to, subject, body, smtp_server="smtp.gmail.com", port=465):
    "Send an email via SMTP"
    msg = EmailMessage()
    msg["From"] = "you@gmail.com"
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)
    
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login("you@gmail.com", "your_password")
        server.send_message(msg)
    
    print("Email sent to {}!".format(to))

# 示例：发送每日报告
if __name__ == "__main__":
    send_email(
        to="boss@example.com",
        subject="Daily Report",
        body="Sales: $1,234"
    )
