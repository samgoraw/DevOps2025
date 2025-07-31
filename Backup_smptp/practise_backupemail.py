import os
import shutil
import smtplib
from datetime import datetime 
from email.message import EmailMessage



def parse_logs(log_path):
      try:
        with open(log_path,"r") as file:
            lines = file.readlines()
        print(f"[+] Parsed {len(lines)} lines from log files.")
        return lines
      except Exception as e:
        print(f"[!]Failed to read log file:{e}")
        return []

         

def create_backup(log_path, backup_folder):
    try:
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(backup_folder, f"log_backup_{timestamp}.log")
        shutil.copy(log_path, backup_file)
        print(f"[+] Backup created at {backup_file}")
        return backup_file
    except Exception as e:
        print(f"[!] Failed to create backup: {e}")
        return None


def check_errors(log_lines):
        error_lines = [line for line in log_lines if "error" in line.lower() ]
        print(f"[+] Found {len(error_lines)} error(s) in log.")
        return error_lines



def send_email(subject,body):
        sender_email = "sam.gourav19@gmail.com"
        receiver_email = "sam.gourav88@hotmail.com"
        password = "skvt zipt wloc yebw"
    
        msg = EmailMessage()
        msg["subject"] = subject
        msg["from"] = sender_email
        msg["to"] = receiver_email
        msg.set_content(body)

        with open('app.log','rb') as f: #rb is read binary and f stands for file
             msg.add_attachment(f.read(),filename ="app.log",maintype = 'text',subtype = 'plain')

        try:

            with smtplib.SMTP("smtp.gmail.com","587") as server:  #use of the smtp server, smtp uses its own server
                server.starttls() #encrypt the connection
                server.login(sender_email,password)
                server.send_message(msg)
            print("[+] Email sent successfully.")
        except Exception as e:
            print(f"[!] Failed to create backup: {e}")
    

def main():
    log_path = "app.log"
    backup_folder = "backups"

    logs = parse_logs(log_path)
    backup_file = create_backup(log_path, backup_folder)
    errors = check_errors(logs)

    if backup_file:
         if errors:
                body = (f"Log backup created successfully.\n\nFound {len(errors)} error(s).\nCheck backup: {backup_file}")
                send_email("ALERT: System Errors Detected", body)
         else:
                body = (f"Log backup created successfully.\nNo errors found.\nBackup Path: {backup_file}")
                send_email("System Log Backup Success", body)

if __name__ == "__main__":
    main()


#In gmail we also have to set the password by going to https://myaccount.google.com/?pli=1  --> security --> App password --> A system generated PWD will be generated
#parse_logs() – reads log file
#create_backup() – saves a backup copy of the log
#check_errors() – scans for errors
#send_email() – sends the log report with the log file attached

#os – to check/create directories
#shutil – to copy files (for backup)
#smtplib – for sending emails via SMTP
#datetime – to generate timestamped backup filenames
#EmailMessage – to structure and send email messages