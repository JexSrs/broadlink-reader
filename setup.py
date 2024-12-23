from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Broadlink Reader",
    version="0.1.0",
    description="A Python CLI tool for learning and capturing IR commands from Broadlink devices, with options for customizable connection settings and command saving.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JexSrs/broadlink-reader",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.11",
)
