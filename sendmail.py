# --- Simple emaling script ---
# usage: sendmail.py subject body

# parameters:
sender = 'postgres@localhost'
receivers = ['monitor@example.com', ]
server = 'smtp.example.com'

# ------------------------------

import smtplib
from email.mime.text import MIMEText
from smtplib import SMTPException
import sys
import subprocess

if len(sys.argv) != 3:
   print "Usage: sendmail.py subject body"
   sys.exit()

subject = str(sys.argv[1])
body = str(sys.argv[2])

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = ", ".join(receivers)

try:
   smtpObj = smtplib.SMTP(server)
   smtpObj.sendmail(sender, receivers, msg.as_string())
   subprocess.call(["logger", "sendmail.py successfully sent email"])
except SMTPException as e:
   subprocess.call(["logger", "ERROR: sendmail.py SMTPException: %s" % e.strerror])

