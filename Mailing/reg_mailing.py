#!/usr/bin/python

import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_user = 'acesvce20@gmail.com'
email_password = 'ace@svce'

emailArray=['blackbugofficial@gmail.com','jeffreyjoan2722001@gmail.com','akshayasrinivas8@gmail.com','kpdrishi@gmail.com','k.srikrish12@gmail.com','rogerthatvivek@gmail.com','krishsaran99@gmail.com','rahularsenal@yahoo.com','dhivyadharshini115@gmail.com','harshinisivanathbabu@gmail.com','gpk.magsun@gmail.com']
iterationLength=len(emailArray)

for i in range(0,iterationLength):

    email_send = emailArray[i]
    subject = "Registration Confirmation, Hackerrupt '20!"

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    # body="Hey there!\nSeeing that you registered for last year's INTERRUPT, SVCE's annual CSE Symposium, we thought you'd like to know that it's BACKK! And it's BIGGER and BETTER than ever!\n\nOffering more than 12 events which are both technical and non-technical, Interrupt 2k18 promises to be an extremely entertaining and fun event! This year, we are holding two online events which include 'Pipe The Piper' (a puzzle-solving challenge) and'Interrupt Challenge', our signature event. There are a lot more interesting and special events which you can participate in on the day of Interrupt itself. To register for these events and get information on other events, check out our cool Linux-themed website www.interrupt2k18.in!\n\nHaving you around last year was something we truly appreciated and we hope to see you this year too! If you haven't already registered for Interrupt 2k18, you should!\n\nYours sincerely,\nTeam Interrupt '18"

    body="Greeting from Hackerrupt’20 team!\n\nThank you for registering!\n\nThe abstract idea you’ve submitted will be reviewed by our panel members and we’ll be notifying you by mail if you’ve been shortlisted.\n\nWe’ll get back to you soon with a confirmation email and discuss the mode of payment as well.\n\nSo till then keep your eyes, ears and inboxes open!\n\nCheers,\nTeam Hackerrupt’20"

    msg.attach(MIMEText(body,'plain'))

    #filename='interrupt_brochure.pdf'	
    #attachment=open(filename,'rb')

    #part = MIMEBase('application','octet-stream')
    #part.set_payload((attachment).read())
    #encoders.encode_base64(part)
    #part.add_header('Content-Disposition',"attachment; filename= "+filename)

    #msg.attach(part)

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)

    server.sendmail(email_user,email_send,text)
    server.quit()

    print("Sent mail to "+email_send)

# The code ends here.

