# coding: utf-8
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import logging


class {{cookiecutter.app_name}}Exception(Exception):
    """
    Unrecoverable error in {{cookiecutter.app_name}}.
    """
    pass


class {{cookiecutter.app_name}}(object):
    """
    {{cookiecutter.app_name}} base class.
    """

    def __init__(self, conf):
    	self.conf = conf