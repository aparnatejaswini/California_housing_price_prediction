from setuptools import setup, find_packages


#Declaring variables for setup functions
PROJECT_NAME = "house-price-predictor"
VERSION = "0.0.1"
AUTHOR="Aparna T Parkala"
DESCRIPTION="Objective of the project is to estimate median housing prices for given district"
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_lists():
    """
    output: List[str]
    Reads requirements.txt and returns libraries mentioned in file as list
    """
    with open(REQUIREMENT_FILE_NAME) as require_file: 
        return require_file.readlines()


setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    packages=find_packages(),
    install_requires=get_requirements_lists()
)