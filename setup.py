#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo_zoho',
    version='1.0',
    description='Connectino zoho plugin',
    author='Mojtaba Karimi',
    author_email='mmojtabakarimi@yahoo.com',
    packages=find_packages(),
    url='https://www.foo-bar.com',
    include_package_data=True,
    package_data={
        'wazo_zoho': ['*/api.yml'],
    },

    entry_points={
        'wazo_auth.external_auth': [
            'zoho = wazo_zoho.plugin:Plugin'
        ]
    }
)
