#!/usr/bin/env python
#
# Copyright 2014 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys

from setuptools import setup, find_packages

LONG_DESCRIPTION = None
README_MARKDOWN = None

with open('README.md') as markdown_source:
    README_MARKDOWN = markdown_source.read()

if 'upload' in sys.argv:
    # Converts the README.md file to ReST, since PyPI uses ReST for formatting,
    # This allows to have one canonical README file, being the README.md
    # The conversion only needs to be done on upload.
    # Otherwise, the pandoc import and errors that are thrown when
    # pandoc are both overhead and a source of confusion for general
    # usage/installation.
    import pandoc
    pandoc.core.PANDOC_PATH = 'pandoc'
    doc = pandoc.Document()
    doc.markdown = README_MARKDOWN
    LONG_DESCRIPTION = doc.rst
else:
    # If pandoc isn't installed, e.g. when downloading from pip,
    # just use the regular README.
    LONG_DESCRIPTION = README_MARKDOWN

setup(
    name='qdb',
    version='0.1.0',
    description='Quantopian Remote Debugger for Python',
    author='Quantopian Inc.',
    author_email='opensource@quantopian.com',
    packages=find_packages(),
    scripts=['client/qdb-cli'],
    long_description=LONG_DESCRIPTION,
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX',
        'Topic :: Software Development :: Debuggers',
    ],
    install_requires=[
        'contextlib2',
        'gevent',
        'gevent-websocket',
        'gipc',
        'Logbook',
        'six',
        'websocket-client',
    ],
    url="https://github.com/quantopian/qdb"
)
