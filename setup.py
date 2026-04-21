from setuptools import setup, find_packages

setup(
    name="home-energy-manager-sax-power",
    version="1.0.0",
    description="package for reading Sax devices",
    url="https://github.com/Hans-4/home-energy-manager-sax-power",
    author="Hannes",
    license="MIT",
    packages=find_packages(),
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "pymodbus==2.5.3"
    ]
)