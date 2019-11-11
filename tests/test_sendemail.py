# -*- coding: utf-8 -*-

import unittest
import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from postmancli.sendemail import send_mail
import base64


class TestSendEmail(unittest.TestCase):

    def test_send(self):
        msg = send_mail("user:password@smtp.gmail.com:465",
                        "user@gmail.com",
                        ["receiver1@gmail.com", "receiver1@gmail.com"],
                        "Test Email",
                        "This is an email test@nl@@tab@Enjoy it!",
                        debug=True)

        self.assertEqual("user@gmail.com", msg.get('From'))
        self.assertEqual("receiver1@gmail.com, receiver1@gmail.com", msg.get('To'))
        self.assertEqual("Test Email", msg.get('Subject'))
        self.assertTrue(msg.get('Message-ID').find('postman-cli.') >= 0)
        self.assertEqual("This is an email test\n\tEnjoy it!", base64.b64decode(msg.get_payload()[0]._payload)
                         .decode('utf-8'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
