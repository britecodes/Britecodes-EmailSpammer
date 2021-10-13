import smtplib, ssl
from email.message import EmailMessage
from easygui import passwordbox
import time
import sys

print("Email spammer \n BY")
print( """
▀█████████▄     ▄████████  ▄█      ███        ▄████████  ▄████████  ▄██████▄  ████████▄     ▄████████    ▄████████ 
  ███    ███   ███    ███ ███  ▀█████████▄   ███    ███ ███    ███ ███    ███ ███   ▀███   ███    ███   ███    ███ 
  ███    ███   ███    ███ ███▌    ▀███▀▀██   ███    █▀  ███    █▀  ███    ███ ███    ███   ███    █▀    ███    █▀  
 ▄███▄▄▄██▀   ▄███▄▄▄▄██▀ ███▌     ███   ▀  ▄███▄▄▄     ███        ███    ███ ███    ███  ▄███▄▄▄       ███        
▀▀███▀▀▀██▄  ▀▀███▀▀▀▀▀   ███▌     ███     ▀▀███▀▀▀     ███        ███    ███ ███    ███ ▀▀███▀▀▀     ▀███████████ 
  ███    ██▄ ▀███████████ ███      ███       ███    █▄  ███    █▄  ███    ███ ███    ███   ███    █▄           ███ 
  ███    ███   ███    ███ ███      ███       ███    ███ ███    ███ ███    ███ ███   ▄███   ███    ███    ▄█    ███ 
▄█████████▀    ███    ███ █▀      ▄████▀     ██████████ ████████▀   ▀██████▀  ████████▀    ██████████  ▄████████▀  
               ███    ███                                                                                          
""")
print("Britecodes new and improved email spammer, pls use responsibly")
email = input("Please enter your email you wish to log into.. ")
password = passwordbox("PASSWORD:")
subinput = input("What do you wish the subject of the email to be?.. ")
contentinput = input("What do you wish the body of the email to say?.. ")
spoofname = input("What do you wish for the name the email comes from to be?.. ")
recipient = input("Enter recipient email address.. ")
repeats = int(input("How many times do you wish to send the email?.. "))
delay = int(input("How many seconds delay do you wish to have between emails?.. "))

if "@gmail.com" in email:
    print("\ngmail detected; assigning port and smtp ssl.")
    port = int('465')
    smtpid = "smtp.gmail.com"
elif "@yahoo.com" in email:
    print("\nYahoo detected;  assigning port and smtp ssl.")
    port = int('465')
    smtpid = "smtp.mail.yahoo.com"
elif "@outlook.com" in email:
    print("\nYahoo detected;  assigning port and smtp ssl.")
    port = int('995')
    smtpid = "smtp-mail.outlook.com"
else:
    print("\n Error invalid email address, this script only supports gmail, yahoo and outlook.")
    time.sleep(4)
    sys.exit()



msg = EmailMessage()
msg['Subject'] = subinput
msg.set_content(contentinput)
msg['From'] = spoofname
msg['To'] = recipient

sslcontext = ssl.create_default_context()

for i in range(0, repeats):
    connection = smtplib.SMTP_SSL(smtpid, port, context=sslcontext)
    connection.login(email, password)
    connection.send_message(msg)
    print("Your message is sent!")
    time.sleep(delay)
