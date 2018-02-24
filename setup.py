#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys
from setuptools import setup


def get_version(*file_paths):
    """Retrieves the version from username_tools/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version("username_tools", "__init__.py")


if sys.argv[-1] == 'publish':
    try:
        import twine
        print("Twine version: ", twine.__version__)
    except ImportError:
        print('Twine library missing. Please run "pip install twine"')
        sys.exit()
    os.system('python setup.py sdist')
    os.system('twine upload dist/*')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-username-tools',
    version=version,
    description="""Username validation fields and utilities for Django""",
    long_description=readme + '\n\n' + history,
    author='keshaB Paudel',
    author_email='self@keshab.net',
    url='https://github.com/poudel/django-username-tools',
    packages=[
        'username_tools',
    ],
    include_package_data=True,
    install_requires=["Django>=2.0.2",],
    license="MIT",
    zip_safe=False,
    keywords='django-username-tools',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
