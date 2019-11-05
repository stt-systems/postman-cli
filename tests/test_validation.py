# -*- coding: utf-8 -*-

import unittest
import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from postmancli.validation import Validator
from argparse import ArgumentTypeError


class TestClassValidations(unittest.TestCase):

    def test_domain(self):
        self.assertEqual('mascandobits.es', Validator.check_domain('mascandobits.es'))
        self.assertEqual('subdomain.mascandobits.es', Validator.check_domain('subdomain.mascandobits.es'))
        self.assertEqual('more-mascandobits.es', Validator.check_domain('more-mascandobits.es'))
        self.assertEqual('subdomain.more-mascandobits.es', Validator.check_domain('subdomain.more-mascandobits.es'))
        try:
            Validator.check_domain('rdch106@mascandobits.es')
            self.fail('Exception not raised')
        except ArgumentTypeError as e:
            self.assertIsInstance(e, ArgumentTypeError)
        try:
            Validator.check_domain('-mascandobits.es')
            self.fail('Exception not raised')
        except ArgumentTypeError as e:
            self.assertIsInstance(e, ArgumentTypeError)
        try:
            Validator.check_domain('.mascandobits.es')
            self.fail('Exception not raised')
        except ArgumentTypeError as e:
            self.assertIsInstance(e, ArgumentTypeError)
        try:
            Validator.check_domain('subdomain.-mascandobits.es')
            self.fail('Exception not raised')
        except ArgumentTypeError as e:
            self.assertIsInstance(e, ArgumentTypeError)
        try:
            Validator.check_domain('-subdomain.mascandobits.es')
            self.fail('Exception not raised')
        except ArgumentTypeError as e:
            self.assertIsInstance(e, ArgumentTypeError)
        try:
            Validator.check_domain('.subdomain.mascandobits.es')
            self.fail('Exception not raised')
        except ArgumentTypeError as e:
            self.assertIsInstance(e, ArgumentTypeError)

    def test_server(self):
        self.assertEqual('user:password@domain.com:443',
                         Validator.check_server('user:password@domain.com:443'))
        self.assertEqual('user:password@subdomain.domain.com:443',
                         Validator.check_server('user:password@subdomain.domain.com:443'))
        self.assertEqual('user:password@more-domain.com:443',
                         Validator.check_server('user:password@more-domain.com:443'))
        self.assertEqual('user:password@subdomain.more-domain.com:443',
                         Validator.check_server('user:password@subdomain.more-domain.com:443'))
        self.assertEqual('user.1:password.1@domain.com:443',
                         Validator.check_server('user.1:password.1@domain.com:443'))
        self.assertEqual('user.1:password.1@more-domain.com:443',
                         Validator.check_server('user.1:password.1@more-domain.com:443'))
        self.assertEqual('user.1:password.1@subdomain.domain.com:443',
                         Validator.check_server('user.1:password.1@subdomain.domain.com:443'))
        self.assertEqual('user.1:password.1@more-subdomain.domain.com:443',
                         Validator.check_server('user.1:password.1@more-subdomain.domain.com:443'))
        self.assertEqual('user.1:password.1@subdomain.more-domain.com:443',
                         Validator.check_server('user.1:password.1@subdomain.more-domain.com:443'))
        self.assertEqual('user.1:password.1@more-subdomain.more-domain.com:443',
                         Validator.check_server('user.1:password.1@more-subdomain.more-domain.com:443'))
        try:
            Validator.check_server('domain.com:443')
            self.fail('Exception not raised')
        except ArgumentTypeError as e:
            self.assertIsInstance(e, ArgumentTypeError)
        try:
            Validator.check_server('user:password@domain.com')
            self.fail('Exception not raised')
        except ArgumentTypeError as e:
            self.assertIsInstance(e, ArgumentTypeError)
        try:
            Validator.check_server('user@domain.com:443')
            self.fail('Exception not raised')
        except ArgumentTypeError as e:
            self.assertIsInstance(e, ArgumentTypeError)
        try:
            Validator.check_server('user:password@-domain.com:443')
            self.fail('Exception not raised')
        except ArgumentTypeError as e:
            self.assertIsInstance(e, ArgumentTypeError)


class TestClassMethods(unittest.TestCase):
    def test_get_main_domain(self):
        self.assertEqual('mascandobits.es', Validator.get_main_domain('mascandobits.es'))
        self.assertEqual('mascandobits.es', Validator.get_main_domain('subdomain.mascandobits.es'))
        self.assertEqual('more-mascandobits.es', Validator.get_main_domain('more-mascandobits.es'))
        self.assertEqual('more-mascandobits.es', Validator.get_main_domain('subdomain.more-mascandobits.es'))
        self.assertEqual('mascandobits.es', Validator.get_main_domain('more-subdomain.mascandobits.es'))
        self.assertEqual('more-mascandobits.es', Validator.get_main_domain('more-subdomain.more-mascandobits.es'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
