import os
import shutil
from datetime import datetime
import logging
import smtplib
from email.mime.text import MIMEText



def send_email(subject,body):
    sender_email = "sam.gourav19@gmail.com"
    receiver_email = "sam.gourav88@hotmail.com"
    password = "ysqb nuwi kxnp qnan"

   #go to https://myaccount.google.com
    # select>security> enable 2 step-verification
    # Search bar > app password
    # create new password and use it

    msg = MIMEText(body)
    msg["subject"] = subject
    msg["from"] = sender_email
    msg["to"] = receiver_email

    with smtplib.SMTP("smtp.gmail.com","587") as server:  #use of the smtp server, smtp uses its own server
        server.starttls()
        server.login(sender_email,password)
        server.send_message(msg)



logging.basicConfig(
      filename = 'backup.log',
      filemode = 'a', #a stands for append
      level = logging.DEBUG,
      format = '%(asctime)s - %(levelname)s - %(message)s'

)


try:

    source_folder = "files"
    backup_folder = "backups"

    os.makedirs(backup_folder,exist_ok = True)

    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

    backup_filename = f"{backup_folder}/backup_{timestamp}"

    shutil.make_archive(backup_filename,'zip',source_folder)
    logging.info(f"Backup created {backup_filename}.zip")
    send_email("Back up completed",f"Backup created {backup_filename}.zip")

except Exception as e:
    logging.error(f"Backup failed:{e}")


   






