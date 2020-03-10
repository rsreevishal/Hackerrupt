#!/usr/bin/python

import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_user = 'acesvce20@gmail.com'
email_password = 'ace@svce'

emailArray=['kabilanelango@gmail.com','preethi5may99@gmail.com','harirohit45@gmail.com','pranavm@gmail.com','vp@yahoo.co.in','ajayr2224@gmail.com','sudarsan123@gmail.com','sahana112@gmail.com','sandy22@gmail.com','vandhana2999@gmail.com','ramanababu@gmail.com','sandy27@gmail.com','kumarsangar111@gmail.com','ramachandran2000@gmail.com','ganeshrpg2001@gmail.com','malarvaani@gmail.com','hemachandran17@gmail.com','rajeshkumar2000@gmail.com','rishikaran987@gmail.com','karthi253@gmail.com','dream11@gmail.com','vizhnu99@gmail.com','udhaya1999@gmail.com','kumuransai@gmail.com','sujithravi05121999@gmail.com','arunajith15@gmail.com','maha.pep@gmail.com','akshaivs65@gmail.com','surajlakkur26@gmail.com','nandhakumarv3318@gmail.com','anbunaveen11@gmail.com','karpagamb1999@gmail.com','rupesh@gmail.com','hasiith007@gmail.com','kvsk1teen@gmail.com','Mohdhassan2609@gmail.com','anifabanu@gmail.com','gunashrie2000@gmail.com ','danielantonyjohn@gmail.com','sibisiddu@gmail.com','sujithukku@gmail.com','veluelumalai05@gmail.com','karthikhero24@gmail.com','a.charan2001@gmail.com','sujithcheeku18@gmail.com','saijanani8@gmail.com','mahi2247@gmail.com','nandhabarathi299@gmail.com','kamalnath2000@gmail.com ','mrjayen99@gmail.com','yokesh560@gmail.com','sooryanagarajan@gmail.com','sudarshan0831@gmail.com','abhishekaniruth@gmail.com','suresh112@gmail.com','sailakshmitrt@gmail.com','aravindkumar@gmail.com','mukeshram@gmail.com','meda.jayesh29@gmail.com','vigneshsrinivasan20000@gmail.com','visves05@gmail.com','evedha28@gmail.com','gomathithirumurthy@gmail.com','renubharathi99@gmail.com','vishnudharshini@gmail.com','jeevamay6@gmail.com','nandhiniram@gmail.com','rakesh1000@gmail.com','vickiivladimir25102000@gmail.com','sachinvicky12357@gmail.com','dhanushbdev@gmail.com','evedha2810@gmail.com','balajikeshav201099@gmail.com','acsvsknsh@gmail.com','someshmsd007@gmail.com','sujeethukku@gmail.com','abhiramani.aa@gmail.com ','rithannyat@gmail.com','benjay@gmail.com','gokulrocks117@gmail.com','veluvirat05@gmail.com','mukilmickey@gmail.com','sibivishnu6@outlook.com','harshithavisvanath@gmail.com','surikumar@gmail.com','samstunner15@gmail.com','monishboy543@gmail.com','yuvimessi@gmail.com','rameshvar@gmail.com','sharonjoseph95@gmail.com','hariharanucm@gmail.com','kourith@gmail.com','gdashwanth36@gmail.com','vijayuditnarayan@gmail.com','logavignesh2000@gmail.com','hebahaseena8@gmail.com','viveksiva98421@gmail.com','selvapreethi.s@gmail.com','monishasrisai@gmail.com','ganeshgopal2001@gmail.com','Parthi11116@gmail.com','tsrpallavi10@gmail.com','nafismd2000@gmail.com','vcujwal@gmail.com','18bcomcaponvenkatesh@gmail.com','harinibhaskaran10@gmail.com','tanveesajith@gmail.com ','ravi123@gmail.com','prakashsakthivel@gmail.com','sudarshan111@gmail.com','ramprasad1995@gmail.com','aashik29@gmail.com','praveen256@gmail.com','indirathangam2000@gmail.com','subashthangam2000@gmail.com','brightvimal@gmail.com','narayana1998@gmail.com','gokulkanna@gmail.com','supraja1652@gmail.com','sushma27500@gmail.com','vikasreddy.kaliki@gmail.com','heera.rajasekar0410@gmail.com','kushaalreddy7@gmail.com','shobhinkh@gmail.com','ramyakumar487@gmail.com','kvviswam444@gmail.com','guruhariharaun2000@gmail.com','rahulmadhavan99@gmail.com','arunagiriselvam374@gmail.com','shriramgobu@gmail.com','maddy.cps@gmail.com','jyuvaraj03@gmail.com','dineshkumarsai182@gmail.com','thaaranij@gmail.com','sudharsansuresh7@gmail.com','14302sai@gmail.com','smartsahari619@gmail.com','yuvashreesenthil@gmail.com','vedhanarayanan28@gmail.com','bharathprabha7131563@gmail.com','stingrose@gmail.com','muthukumarvishwanathan0411@gmail.com','smeritheegovi@gmail.com','mailtosridharmoorthy@gmail.com','naveenbalaji737@gmail.com','vivekece1999@outlook.com','sangeethachandrakumar@yahoo.com','athmaja1506@gmail.com','vishakarudhra@gmail.com','siva2000.rangu@gmail.com','kailash.s1998@gmail.com','sweetylovechoco@gmail.com','sathyasudhanoo4@gmail.com','suriyakumari2709@gmail.com','rakshanasri2512@gmail.com','vicchi9915@gmail.com','madeshmaddy23@gmail.com','shivashankar1598@gmail.com','pranavraaj18@gmail.com','yageswaran.a@gmail.com','vinobheem23@gmail.com','priyadharshini.s.2017.cse@ritchennai.edu.in','gurudharshan.n.2018.cse@ritchennai.edu.in','chintha.s.k.priya@gmail.com','svdharshan01@gmail.com','damondharan@gmail.com','sudeepakmpt@gmail.com','chintha.s.ratna@gmail.com','guhanbalakrishnan20@gmail.com','nithyakrishnan117@gmail.com','reethika2233@gmail.com','adithya.lavanya@gmail.com','nivetha.m.2017.cse@ritchennai.edu.in','kanakag02@gmail.com','jagathratchagankarthi@gmail.com','tharaniwinx@gmail.com','srihariram80@gmail.com','bharathvyas07@gmail.com','vickymeera15@gmail.com','madhanraj.life1441@gmail.com']
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

