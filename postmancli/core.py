# -*- coding: utf-8 -*-

import argparse
from postmancli.sendemail import send_mail
from postmancli.validation import Validator
from postmancli.metadata import Metadata


class Postman(object):

    def __init__(self):
        self.meta = Metadata()

        # Parse arguments provided
        parser = argparse.ArgumentParser()
        parser.add_argument('-v', '--version', action='version', version=self.meta.get_version())
        parser.add_argument('-S', '--server', dest='server',
                            help="SMTP server with format user:password@smtpserver:port",
                            type=Validator.check_server, required=True)
        parser.add_argument('-f', '--from', dest='msg_from', help="Sender email address", required=True)
        parser.add_argument('-t', '--to', dest='msg_to', nargs='+', help="Receiver email address", required=True)
        parser.add_argument('-s', '--subject', dest='subject', help="Email subject", required=True)
        parser.add_argument('--text', dest='text', help="Email body (plain text)", default="", required=False)
        parser.add_argument('-a', '--attachment', dest='attachment', nargs='+',
                            help="One or more files to attach", default=[], required=False)
        self.args = parser.parse_args()

    def run(self):
        server_values = Validator.get_server_values(self.args.server)
        if len(server_values[0].split("@")) == 1:
            server_values[0] = server_values[0] + '@' + Validator.get_main_domain(server_values[2])
        send_mail({'user': server_values[0], 'password': server_values[1],
                   'host': server_values[2], 'port': int(server_values[3])},
                  msg_from=self.args.msg_from, msg_to=self.args.msg_to, subject=self.args.subject, text=self.args.text,
                  files=self.args.attachment)


if __name__ == "__main__":
    postman = Postman()
    postman.run()
