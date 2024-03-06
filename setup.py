from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()


setup(
name='carsanalyzer',
version='0.1.0',
description='a package that analyzes cars dataset',
package_dir={"":"app"},
packages=find_packages(where="app"),
long_description=long_description,
long_description_content_type="text/markdown",
url="https://github.com/tdrv90/cars",
author='Alexander Todorov',
author_email="al.todorov@outlook.com",
license="MIT",
classifiers=[
    "License :: MIT License",
    "Programming Language :: Python",
    "Operating System :: OS Independent"
],
install_requires=["pandas"]
)