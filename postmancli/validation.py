# -*- coding: utf-8 -*-

import re
import argparse


class Validator(object):
    __domain_pattern = re.compile("^([a-z0-9]+(\-[a-z0-9]+)*\.)+[a-z]{2,3}$")
    __main_domain_pattern = re.compile("([a-z0-9]+(\-[a-z0-9]+)*\.){1}[a-z]{2,3}$")
    __server_pattern = re.compile("^([\w\.]+){1}:([\w\.]+){1}@([\w\-\.]+){1}:(\d+){1}$")

    @staticmethod
    def check_domain(string):
        if Validator.__domain_pattern.match(string):
            return string
        else:
            raise argparse.ArgumentTypeError("%s is not valid domain" % string)

    @staticmethod
    def check_server(string):
        ret = Validator.__server_pattern.match(string)
        if ret:
            tmp_val = string.split("@")
            if len(tmp_val) == 2:
                tmp_val = tmp_val[1].split(":")
                if len(tmp_val) == 2:
                    if Validator.check_domain(tmp_val[0]):
                        return string
        raise argparse.ArgumentTypeError("%s is not valid server format.\n"
                                         "Try to use following format: user:password@smtpserver:port" % string)

    @staticmethod
    def get_main_domain(domain):
        main_domain = Validator.__main_domain_pattern.search(domain)
        return main_domain.group(0)

    @staticmethod
    def get_server_values(server):
        values = server.split(':')
        tmp = values[1].split('@')
        values[1] = tmp[0]
        values.insert(2, tmp[1])
        return values
