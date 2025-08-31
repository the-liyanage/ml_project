from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
        this function will return the list of requirements
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

setup(
    name = 'mlproject',
    version = 0.01,
    author = 'hiruni',
    author_email='hiruniliyanage4@gmail.com',
    packages= find_packages(),
    install_requires = ['pandas', 'seaborn', 'numpy']
)