# TASK 3: Email sending

import yagmail 

# Initialize the connection
yag = yagmail.SMTP('bairwabhupendra98@gmail.com', 'cphn pxpx luks bclk')

# Send the email
yag.send(
    to='receiver email',
    subject='Hello from Python!',
    contents='This is a test email sent using Python with yagmail!'
)

print("Email sent successfully using yagmail!")