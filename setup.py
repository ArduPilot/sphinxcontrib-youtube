#-*- coding:utf-8 -*-

import setuptools


setuptools.setup(
    name='sphinxcontrib.youtube',
    version='100.4.1',
    packages=setuptools.find_packages(),
    install_requires=[
        'sphinx',
        'requests',
        ],
    url='https://github.com/ArduPilot/sphinxcontrib-youtube',
    description='''embedding youtube videos into sphinx''',
    namespace_packages=['sphinxcontrib'],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Utilities",
        ]
)
