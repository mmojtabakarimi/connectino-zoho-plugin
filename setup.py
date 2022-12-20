#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo-zoho',
    version='1.0',
    description='Connectino zoho plugin',
    author='Mojtaba Karimi',
    author_email='mmojtabakarimi@yahoo.com',
    packages=find_packages(),
    url='https://www.foo-bar.com',
    include_package_data=True,
    package_data={
        'wazo_auth_zoho': ['api.yml'],
    },

    entry_points={
        'wazo_auth.plugins': [
            'zoho = wazo_auth_zoho.plugin:Plugin'
        ]
    }
)
