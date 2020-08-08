# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

setup(
    name="pypper",
    version="0.1.2",
    description="A developer toolbox not only for Python",
    author="Yunbo WANG",
    author_email="w.yunbo@gmail.com",
    url="https://github.com/iyunbo/pypper",
    license="MIT License",
    long_description_content_type="text/markdown",
    long_description=readme,
    packages=find_packages(exclude=("tests", "docs"))
)
