import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials
sender_email = "bairwabhupendra98@gmail.com"
sender_password = "cphn pxpx luks bclk"  # Use App Password if Gmail
receiver_email = "bhupendrabairwaqq2345@gmail.com"

# Create the email
subject = "Hello from Python!"
body = "This is a test email sent using Python."

# Set up the MIME
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

# Connect to the Gmail SMTP server and send the email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Upgrade the connection to secure
    server.login("bairwabhupendra98@gmail.com", "Bhu&562004")
    server.sendmail("bairwabhupendra98@gmail.com", "bhupendrabairwaqq2345@gmail.com", message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()
