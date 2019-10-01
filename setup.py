"""
lambdata - a collection of data science helper functions for lambda school
"""

import setuptools

REQUIRED = [
    "numpy",
    "pandas"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    setuptools.setup(
    name="lambdata-ldtownsend",
    version = "0.1.2",
    author= "ldtownsend",
    description = "a collection of data science helper funcitons, 2 added",
    long_description = LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://lambdaschool.com",
    packages=setuptools.find_packages(),
    python_requires = ">= 3.5",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
   )
