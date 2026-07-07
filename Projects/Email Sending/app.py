# import required modules
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Server Configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = " Enter Your email@gmail.com"
passkey = "Enter your 16 digit App Password"


def singleEmailSend(to_email:str, subject:str, body:str):
    msg= MIMEMultipart()
    msg['FROM' ]= sender_email
    msg['TO']= to_email
    msg['Subject']=subject
    msg.attach(MIMEText(body,"plain"))

    try:
        # start server
        server =SMTP(smtp_server, smtp_port)
        # start server 
        server.starttls()
        # login to server
        server.login(sender_email,passkey)
        # send email
        server.sendmail(sender_email,to_email,msg.as_string())
        server.quit()
        return f"Succesfully email send to {to_email}"
    except Exception as e:
        return f"Failed to Send email :{e}"

# 
to_email= input("Enter Email address:")
subject = input("Enter Email Subject:")
body=input("Enter Email Body:")
# call singleEmailSend
print(singleEmailSend(to_email,subject,body))