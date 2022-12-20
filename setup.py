#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo_zoho',
    version='0.1',
    description='Wazo ZOHO',

    author='Wazo Authors',
    author_email='dev@wazo.io',

    url='http://wazo.io',

    packages=find_packages(),
    include_package_data=True,
    package_data={
        'wazo_zoho': ['*/api.yml'],
    },
    entry_points={
        'wazo_auth.external_auth': [
            'zoho = wazo_zoho.auth.plugin:Plugin',
        ],
    }
)
