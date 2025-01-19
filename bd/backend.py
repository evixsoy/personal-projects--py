#zlepsit mozna look emailu
#hostovani
#napsat v emailu kolik oslavuje user let

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl
import schedule
import time
import datetime


def action():
    x = datetime.datetime.now()
    dayrl = x.day
    monthrl = x.month
    yearrl = x.year
    daterl = f"{dayrl}/{monthrl}"
    
    with open("date.env") as dateopen:
        filefinddate = dateopen.read()
    with open("name.env") as nameopen:
        filefindname = nameopen.read()
    with open("year.env") as yearopen:
        filefindyear = yearopen.read()

    #splitnou dates a jmena
    datelist =filefinddate.split("|")
    namelist =filefindname.split("|")
    yearlist = filefindyear.split("|")
    # check na jakym miste je dnesni datum v listu narozenin
    count = 0
    found = 0
    foundplace = 0
    
    for i in datelist:
        count = count +1
        if i == daterl:
            foundplace = count
            found = 1
            print(f"{namelist[foundplace-1]}: {datelist[foundplace-1]}/{yearlist[foundplace-1]}")
            yearsold = yearrl - int((yearlist[foundplace-1]))
            #email start
            # #email parametry
            sender = "#"
            senderpass = "#"
            receiver = "#"
            #message
            html_content = f"""
            <html>
                <body>
                    <p><strong><span style="font-size: 16px;">NAROZENINY MÁ {namelist[foundplace-1]} oslavuje {yearsold}let!</span></strong></p>
                    <p>Další obsah e-mailu.</p>
                </body>
            </html>
            """
            #message parametry
            message = MIMEMultipart("alternative")
            message['From'] = sender
            message['To'] = receiver
            message['Subject'] = "🎉BIRTHDAY CHECK🎉"

            html_part = MIMEText(html_content, "html")
            message.attach(html_part)
            #odeslani emailu
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
                smtp.login(sender,senderpass)
                smtp.sendmail(sender,receiver,message.as_string())
            print("Email Sent")

    if found ==0:
        print("NIKDO NEMA NAROZENINY")

    

#schedule.every().day.at(00:00).do(action)
schedule.every(10).seconds.do(action)
while True:
    print("Start")
    while True:
        schedule.run_pending()
        time.sleep(1)


