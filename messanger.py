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

