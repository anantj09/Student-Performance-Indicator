from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = "-e ."
def get_requirements(file_path:str)->List[str] :
    '''
    Docstring for get_requirements
    
    :param file_path: get the path of requirements.txt file
    :type file_path: str
    :return: a list contaning all libraries present inside requirements.txt
    :rtype: List[str]
    '''
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    
    return requirements

setup(
    name='Student Performance Indicator',
    version='0.0.1',
    author='Anant Jain',
    author_email='ja.jainanant@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)