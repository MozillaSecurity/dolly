#!/usr/bin/env python
# coding: utf-8
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
{{cookiecutter.app_short_description}}
"""
import os
import sys
import logging
import argparse

from core.{{cookiecutter.repo_name}} import {{cookiecutter.app_name}}, {{cookiecutter.app_name}}Exception
from core.config import {{cookiecutter.app_name}}Conf


class {{cookiecutter.app_name}}CommandLine(object):
    """
    Command-line interface for {{cookiecutter.app_name}}
    """
    HOME = os.path.dirname(os.path.abspath(__file__))
    VERSION = "{{cookiecutter.app_version}}"
    CONFIG_PATH = os.path.relpath(os.path.join(HOME, 'conf'))
    {{cookiecutter.app_name.upper()}}_CONFIG = os.path.join(CONFIG_PATH, '{{cookiecutter.repo_name}}.json')

    @classmethod
    def parse_args(cls):
        parser = argparse.ArgumentParser(description='{{cookiecutter.app_name}} Runtime',
                                         prog=__file__,
                                         add_help=False,
                                         formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                         epilog='The exit status is 0 for non-failures and 1 for failures.')

        m = parser.add_argument_group('Mandatory Arguments')
        g = m.add_mutually_exclusive_group(required=True)
        g.add_argument('-foob', metavar='foo', type=str, help='foo')

        o = parser.add_argument_group('Optional Arguments')
        o.add_argument('-{{cookiecutter.repo_name}}', metavar='file', type=argparse.FileType(), default=cls.{{cookiecutter.app_name.upper()}}_CONFIG,
                       help='{{cookiecutter.app_name}} configuration')
        o.add_argument('-verbosity', metavar='{1..5}', default=2, type=int, choices=list(range(1, 6, 1)),
                       help='Level of verbosity for logging module.')
        o.add_argument('-h', '-help', '--help', action='help', help=argparse.SUPPRESS)
        o.add_argument('-version', action='version', version='%(prog)s {}'.format(cls.VERSION), help=argparse.SUPPRESS)

        return parser.parse_args()

    @staticmethod
    def pair_to_dict(args):
        return dict(kv.split('=', 1) for kv in args)

    @classmethod
    def main(cls):
        args = cls.parse_args()

        logging.basicConfig(format='[{{cookiecutter.app_name}}] %(asctime)s %(levelname)s: %(message)s',
                            level=args.verbosity * 10,
                            datefmt='%Y-%m-%d %H:%M:%S')

        logging.info('Loading {{cookiecutter.app_name}} configuration from %s' % args.{{cookiecutter.repo_name}}.name)
        try:
            {{cookiecutter.repo_name}}_conf = {{cookiecutter.app_name}}Conf(args.{{cookiecutter.repo_name}}.read())
        except {{cookiecutter.app_name}}Exception as msg:
            logging.error(msg)
            return 1

        {{cookiecutter.repo_name}} = {{cookiecutter.app_name}}({{cookiecutter.repo_name}}_conf)
        try:
            pass
        except {{cookiecutter.app_name}}Exception as msg:
            logging.error(msg)
            return 1
        except KeyboardInterrupt:
            print('')
            logging.info("Caught SIGINT - Aborting.")
            return 0
        finally:
            logging.info("Initiating shutdown routines.")
            try:
                pass
            except {{cookiecutter.app_name}}Exception as msg:
                logging.error(msg)
                return 1

        return 0


if __name__ == '__main__':
    sys.exit({{cookiecutter.app_name}}CommandLine().main())
