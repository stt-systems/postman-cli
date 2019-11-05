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
        parser.add_argument('-f', '--from', dest='from', help="Sender email address", required=True)
        parser.add_argument('-t', '--to', dest='to', help="Receiver email address", required=True)
        parser.add_argument('-s', '--subject', dest='subject', help="Email subject", required=True)
        parser.add_argument('--text', dest='text', help="Email body (plain text)", required=False)
        parser.add_argument('-a', '--attachment', dest='attachment', nargs='+',
                            help="One or more files to attach", required=False)
        self.args = parser.parse_args()

    def run(self):
        pass


if __name__ == "__main__":
    postman = Postman()
    postman.run()
