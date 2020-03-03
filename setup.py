# coding: utf-8

import setuptools

with open("README.md", "r") as source:
    long_description = source.read()

setuptools.setup(
    name="fala-parlamentar",
    version="0.0.5",
    author="Jeferson Alves",
    author_email="ferreira.jefersonn@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jefersonalves/fala-parlamentar",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires = [

    ],
    install_requires=[
        "beautifulsoup4>=4.6.3",
        "pandas>=0.23.4",
        "requests>=2.20.0"
    ],
    include_package_data=True,
    python_requires='>=3.6',
)