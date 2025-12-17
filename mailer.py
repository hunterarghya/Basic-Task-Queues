# mailer.py
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASS = os.getenv('SMTP_PASS')

def send_email_logic(to_address, subject, url_link):
    # Create the container email message
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = to_address

    # Create HTML body with a clickable link
    html = f"""
    <html>
      <body>
        <p>Hello,<br>
           Rivers in the seas:<br>
           <a href="{url_link}">Click here to open the URL</a>
        </p>
      </body>
    </html>
    """
    
    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
        s.login(SMTP_USER, SMTP_PASS)
        s.send_message(msg)
    return f"Email sent to {to_address}"