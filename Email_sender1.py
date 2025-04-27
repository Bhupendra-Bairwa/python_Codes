import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("bairwabhupendra98@gmail.com", "cphn pxpx luks bclk")
# message to be sent
message = "Message_you_need_to_send"
# sending the mail
s.sendmail("bairwabhupendra98@gmail.com", "bhupendrabairwaqq2345@gmail.com", message)
# terminating the session
s.quit()
