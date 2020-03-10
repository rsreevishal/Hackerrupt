#!/usr/bin/python

import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_user = 'acesvce20@gmail.com'
email_password = 'ace@svce'

emailArray=['kabilanelango@gmail.com','preethi5may99@gmail.com’,’harirohit45@gmail.com’,’pranavm@gmail.com’,’vp@yahoo.co.in’,’ajayr2224@gmail.com’,’sudarsan123@gmail.com']
iterationLength=len(emailArray)

for i in range(0,iterationLength):

    email_send = emailArray[i]
    subject = "Invite to participate in Hackerrupt '20!"

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    # body="Hey there!\nSeeing that you registered for last year's INTERRUPT, SVCE's annual CSE Symposium, we thought you'd like to know that it's BACKK! And it's BIGGER and BETTER than ever!\n\nOffering more than 12 events which are both technical and non-technical, Interrupt 2k18 promises to be an extremely entertaining and fun event! This year, we are holding two online events which include 'Pipe The Piper' (a puzzle-solving challenge) and'Interrupt Challenge', our signature event. There are a lot more interesting and special events which you can participate in on the day of Interrupt itself. To register for these events and get information on other events, check out our cool Linux-themed website www.interrupt2k18.in!\n\nHaving you around last year was something we truly appreciated and we hope to see you this year too! If you haven't already registered for Interrupt 2k18, you should!\n\nYours sincerely,\nTeam Interrupt '18"

    body="Hello fellow peers,\n\nThe Association of Computer Engineers from the Department of Computer science of Sri Venkateswara College of Engineering is proud to announce it’s first-ever hackathon – Hackerrupt’20.\n\nHackerrupt’20 is our maiden venture into finding young minds and presenting them with the right platform where they can showcase their talents and ideas across various domains of the computer world.\n\nThe 24-hour hackathon will be conducted at the Guvi Geek Network Pvt. Ltd. workspace at the IITM Research Park on the 21st and 22nd of March,2020. The participants will be shortlisted after an initial selection process.\n\nCompete in our 24-hr warfare and stand a chance to win exciting internship opportunities and exclusive goodies. Give in your active participation and take away total prize pool worth 50k.\n\nWe plan on making this event a wonderful experience for all participants to cultivate their skills and build on their dream projects all the while having the best of their times at our hackathon.\n\nFor further details, please visit the website www.hackerrupt.in\n\nThanks and Regards,\nTeam ACE-Hackerrupt’20\nSVCE, CSE"
    msg.attach(MIMEText(body,'plain'))

    filename='hackerrupt_poster.jpeg'	
    attachment=open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)

    server.sendmail(email_user,email_send,text)
    server.quit()

    print("Sent mail to "+email_send)

# The code ends here.

