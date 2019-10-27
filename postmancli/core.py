# -*- coding: utf-8 -*-

import argparse
from postmancli.sendemail import send_mail
from postmancli.metadata import Metadata


class Postman(object):

    def __init__(self):
        self.meta = Metadata()

        # Parse arguments provided
        parser = argparse.ArgumentParser()
        parser.add_argument('-v', '--version', action='version', version=self.meta.get_version())
        self.args = parser.parse_args()

    def run(self):
        pass


if __name__ == "__main__":
    postman = Postman()
    postman.run()
