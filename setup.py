from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)-> List[str]:
    '''
    This funtion return the list of requirements in requirements.txt
    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
        for line in file_obj: 
            req = line.strip()
            if not req or req.startswith('#'):
                continue
            if req == "-e .":
                continue
            requirements.append(req)  
    return requirements        



setup(
    name = "Ml-project", 
    version= "0.0.1", 
    author= "Palak Nagar", 
    author_email= "palaknagar13@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements("requirements.txt")
)