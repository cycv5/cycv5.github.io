import sys
import smtplib
from email.mime.text import MIMEText

def send_email(message):
    sender = 'charlestsai0919@gmail.com'
    recipient = 'charles.cai@mail.utoronto.ca'
    subject = 'Message from Webpage'
    body = message

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient


    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, "gvll tcmm lkmh sadp")
            server.sendmail(sender, recipient, msg.as_string())
        print('Message sent successfully. Thank you!')
    except Exception as e:
        print(f'Sorry, messaging service is currently down: {e}')

if __name__ == "__main__":
    message = sys.argv[1]
    send_email(message)