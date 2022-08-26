from setuptools import setup, find_packages
from typing import List


#decalring variables

PROJECT_NAME="housing-predictor"
VERSION = "0.0.3"
AUTHOR= "bhagyashri"
DESCRIPTION= "this is my ml project"
REQUIREMENT_FILE="requirements.txt"


def get_requiemetns_list()-> List[str]:
    """
    description: this function is going return list the requirement mentioned 
    in the requirement.txt file
    retun this function is going return a list of name of libraries mentions in the 
    requirement.txt file

    """

    with open (REQUIREMENT_FILE) as requirement_file:
        return requirement_file.readlines().remove("-e .")

if __name__=="__main__":
    print(get_requiemetns_list())


setup(name=PROJECT_NAME,
version=VERSION ,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(), #["housing"]
install_requires= get_requiemetns_list() )

