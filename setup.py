from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
        this function will return the list of requirements
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]

        #checking the hypen e dot exists

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements        

setup(
    name = 'mlproject',
    version = 0.01,
    author = 'hiruni',
    author_email='hiruniliyanage4@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)