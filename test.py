from typing import List
import os
def get_requirements(file_path:str)-> List[str]:
    '''
    This funtion return the list of requirements in requirements.txt
    '''
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found")

    
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

get_requirements("requirements.txt")    