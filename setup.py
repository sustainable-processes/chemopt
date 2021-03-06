# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='chemopt',
    version='0.1.0',
    python_requires='==3.*,>=3.6.0',
    author='lightingghost',
    author_email='',
    packages=['chemopt'],
    package_dir={"": "."},
    package_data={
        "chemopt": [
            "*.json", "*.md", "pics/*.png", "save/*.data-00000-of-00001",
            "save/*.index", "save/*.json", "save/*.meta", "save/1/*.json"
        ]
    },
    install_requires=['matplotlib==3.*,>=3.2.1', 'tensorflow==1.13.1'],
    extras_require={"dev": ["pytest==5.*,>=5.2.0"]},
)
