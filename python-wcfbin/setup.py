import os
from setuptools import setup

setup(
    name = "wcf-binary parser",
    version = "0.5.3",
    author = "Timo Schmid",
    author_email = "tschmid@ernw.de",
    description = ("A library for transforming wcf-binary data from and to xml"),
    license = "BSD",
    keywords = "wcf wcf-binary xml",
    url = "",
    packages=['wcf', 'wcf.records', 'tests'],
    scripts=['wcf2xml.py', 'xml2wcf.py'],
    long_description="",
    test_suite="tests.alltests.Suite",
    install_requires=["future"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
