from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
   '''
   this function will return a list of requirements
   '''
   requirements=[]
   with open(file_path) as file_obj:
        requirements=file_obj.readlines()
    #   all the library read from the requirements.txt file
    #   when read the libraries which can be installed its also return \n after library name that's we remove first \n
        requirements=[i.replace("\n","") for i in requirements]

        if(HYPEN_E_DOT in requirements):
            requirements.remove(HYPEN_E_DOT)

   return requirements
         
setup(
    name='mlproject',
    version='0.0.1',
    author='Harsh',
    author_email='harshp6065@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)