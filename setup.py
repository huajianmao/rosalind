# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Rosalind',
    version='0.1.0',
    description='Problem solutions of Rosalind.info',
    long_description=readme,
    author='Huajian Mao',
    author_email='huajianmao@gmail.com',
    url='https://github.com/huajianmao/rosalind',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
