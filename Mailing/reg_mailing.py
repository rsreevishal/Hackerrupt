#!/usr/bin/python

import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_user = 'acesvce20@gmail.com'
email_password = 'ace@svce'

emailArray=['jakekallarackal@gmail.com']
iterationLength=len(emailArray)

for i in range(0,iterationLength):

    email_send = emailArray[i]
    subject = "Registration Confirmation, Hackerrupt '20!"

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body="Greeting from Hackerrupt’20 team!\n\nThank you for registering!\n\nThe abstract idea you’ve submitted will be reviewed by our panel members and we’ll be notifying you by mail if you’ve been shortlisted.\n\nWe’ll get back to you soon with a confirmation email and discuss the mode of payment as well.\n\nSo till then keep your eyes, ears and inboxes open!\n\nCheers,\nTeam Hackerrupt’20"

    msg.attach(MIMEText(body,'plain'))

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)

    server.sendmail(email_user,email_send,text)
    server.quit()

    print("Sent mail to "+email_send)

# The code ends here.

