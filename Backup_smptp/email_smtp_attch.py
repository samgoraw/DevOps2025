import smtplib
from email.message import EmailMessage

def send_email(subject,body):
    sender_email = "sam.gourav19@gmail.com"
    receiver_email = "sam.gourav88@hotmail.com"
    password = "ysqb nuwi kxnp qnan"

    msg = EmailMessage()
    msg["subject"] = subject
    msg["from"] = sender_email
    msg["to"] = receiver_email
    msg.set_content(body)


    with open('app.log','rb') as f: #rb is read binary and f stands for file
        msg.add_attachment(f.read(),filename ="app.log",maintype = 'text',subtype = 'plain')
       

    with smtplib.SMTP("smtp.gmail.com","587") as server:  #use of the smtp server, smtp uses its own server
        server.starttls() #encrypt the connection
        server.login(sender_email,password)
        server.send_message(msg)

send_email("Back up completed","Please find the attached critical error logs!!")

#In gmail we also have to set the password by going to https://myaccount.google.com/?pli=1  --> security --> App password --> A system generated PWD will be generated
