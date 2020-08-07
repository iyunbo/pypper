# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    project_license = f.read()

setup(
    name='pypper',
    version='0.1.0',
    description='A developer toolbox not only for Python',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Yunbo WANG',
    author_email='w.yunbo@gmail.com',
    url='https://github.com/iyunbo/pypper',
    license=project_license,
    packages=find_packages(exclude=('tests', 'docs'))
)
