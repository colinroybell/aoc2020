"""Minimal setup file for aoc2020 project."""

from setuptools import setup, find_packages

setup(
    name='aoc2020',
    version='1.0.0',
    license='proprietary',
    description='Advent of Code 2020',

    author='Colin Bell',
  
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
