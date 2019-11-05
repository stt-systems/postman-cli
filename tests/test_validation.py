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
        try:
            Validator.check_domain('rdch106@mascandobits.es')
            self.fail('Exception not raised')
        except ArgumentTypeError as e:
            self.assertIsInstance(e, ArgumentTypeError)


if __name__ == '__main__':
    unittest.main(verbosity=2)
