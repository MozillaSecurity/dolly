#!/usr/bin/env python
# coding: utf-8
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
test_{{ cookiecutter.repo_name }}
----------------------------------
Tests for '{{ cookiecutter.repo_name }}' module.
"""

import unittest

from {{ cookiecutter.repo_name }} import {{ cookiecutter.repo_name }}


class Test{{ cookiecutter.repo_name|capitalize }}(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

