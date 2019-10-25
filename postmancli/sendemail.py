# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import os
import time
import random


def generate_message_id(msg_from):
    domain = msg_from.split("@")[1]
    r = "%s.%s" % (time.time(), random.randint(0, 100))
    mid = "<%s@%s>" % (r, domain)
    return mid


def send_mail(msg_from, to, subject, text, files=[], server="localhost", debug=False):
    assert type(to) == list
    assert type(files) == list

    msg = MIMEMultipart()
    msg['From'] = msg_from
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    text = text.encode("utf-8")
    text = MIMEText(text, 'plain', "utf-8")
    msg.attach(text)

    msg.add_header('Message-ID', generate_message_id(msg_from))

    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(file,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
        msg.attach(part)

    if not debug:
        smtp = smtplib.SMTP(server)
        smtp.sendmail(msg_from, to, msg.as_string())
        smtp.close()

    return msg
