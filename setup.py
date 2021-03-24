"""Minimal setup file for pyplace package"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyplace',
    version='0.6.9',
    description='A littler utility to stop remembering tons of numbers and star using percentages for containers size and placement.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://volatileprogramming.org",
    project_urls={
        "Source Code": "https://github.com/volatile-programming/pyplace",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(where="src"),
    package_dir={'': 'src'},

    # metadata
    author="Jeffrey I. Jose",
    author_email="jeffrey@volatileprogramming.org",
    license='GNU',
    python_requires='>=3.6'
)