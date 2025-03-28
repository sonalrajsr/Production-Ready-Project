from setuptools import setup, find_packages

setup(
    name="us_visa",
    version="0.0.0",
    author="Sonal Raj",
    author_email='sonalraj0852@gmail.com',
    packages=find_packages(),
)

# This setup.py file is used to package the project(us_visa) as a Python package. It includes metadata about the package, such as its name, version, author, and email. The find_packages() function automatically discovers all packages and subpackages in the project directory.
# This allows the package to be easily installed and distributed using tools like pip.
# This will find all __init__.py files in the directory and create a package structure for the project.
# The setup.py file is a standard way to package Python projects, making it easier to distribute and install them.