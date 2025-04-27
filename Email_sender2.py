import os 
from email.message import Emailmessage
import ssl
import smtplib

email_sender = 'bairwabhupendra98@gmail.com'
email_password = os.environ.get("cphn pxpx luks bclk")
email_receiver = 'bhupendrabairwaq2345@gmail.com'

subject = 'Python Program '
body = """ This is a Python Program by which we can send an email"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())