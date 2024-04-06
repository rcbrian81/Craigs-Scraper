from email.message import EmailMessage
from log import log
import smtplib
import time
import os


email = os.environ.get('my_email')
alert_message = 'Craigs Alert LS: '


def send_emails(emails_content):
    log(f"sending {len(emails_content)} emails.")
    if len(emails_content) > 0:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        for title in emails_content:
            url = emails_content[title]

            message = f'Craigs_Scraper Alert LD: {title} \n {title} \n{url}'
            text = f'Subject: {alert_message}\n\n{message}'

            

            server.login(email, os.environ.get('email_password'))
            server.sendmail(email, email, text)
            time.sleep(5)
        server.quit()

from twilio.rest import Client


def send_sms(matches):
    log(f"sending {len(matches)} SMSes.")
    account_sid = os.environ.get('twilio_sid')
    auth_token = os.environ.get('twilio_token')
    client = Client(account_sid, auth_token)
    for title in matches:
        url = matches[title]
        message = f"{alert_message} \n\n {title} \n\n {url}"
        message = client.messages.create(
            body=message,
            from_='7608284115',
            to=os.environ.get('my_number')
        )


    
