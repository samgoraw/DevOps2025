import smtplib
from email.mime.text import MIMEText

def send_email(subject,body):
    sender_email = "sam.gourav19@gmail.com"
    receiver_email = "sam.gourav88@hotmail.com"
    password = "ysqb nuwi kxnp qnan"

    msg = MIMEText(body)
    msg["subject"] = subject
    msg["from"] = sender_email
    msg["to"] = receiver_email

    with smtplib.SMTP("smtp.gmail.com","587") as server:  #use of the smtp server, smtp uses its own server
        server.starttls()
        server.login(sender_email,password)
        server.send_message(msg)

send_email("Back up completed","Back up created successfully!!")

#In gmail we also have to set the password by going to https://myaccount.google.com/?pli=1  --> security --> App password --> A system generated PWD will be generated
