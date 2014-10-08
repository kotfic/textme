import os
import argparse
import smtplib
from email.MIMEText import MIMEText


def textme(message, subject="Automated Text"):

    gmailUser = os.environ['TEXTME_FROM_EMAIL']
    gmailPassword = os.environ['TEXTME_PASSWORD']
    recipient = os.environ['TEXTME_TO_EMAIL']

    msg = MIMEText(message)
    msg['From'] = gmailUser
    msg['To'] = recipient
    msg['Subject'] = subject

    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmailUser, gmailPassword)
    mailServer.sendmail(gmailUser, recipient, msg.as_string())
    mailServer.close()


def main():
    parser = argparse.ArgumentParser(description="To Write")
    parser.add_argument("message",
                        help="Message to send")

    args = parser.parse_args()

    textme(args.message)


if __name__ == "__main__":
    main()
