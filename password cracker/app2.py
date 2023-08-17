from email.message import EmailMessage
from confige import password
import ssl
import smtplib

email_sender = 'martin4dtruth2@gmail.com'
email_password = password

email_receiver = ['martin4dtruth@gmail.com', 'mar0akporeha1@gmail.com', 'danielbernard329@gmail.com']

subject = "Hello guys how are you this message is to check on you all THANKS"
body = """
LET ME HERE BACK 
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] =subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())