from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."


def get_requirements(file_path:str)->List[str]:
    """
        this will return a list of requirements like -> ["pandas","numpy",.....etc]
    """
    requirements=[]
    with open(file_path) as fileobj:
        requirements = fileobj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements






setup(

    name="AL-based Multi-Disease Prediction System",
    version="0.0.0.1",
    author="Sudipta Roy",
    packages=find_packages(),
    author_email="rsudipta670@gmail.com",
    install_requires=get_requirements('requirements.txt')
)