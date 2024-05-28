from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(filename:str) -> List[str]:
    with open(filename) as f:
        requirements = f.readlines()
        requirements = [r.replace("\n", "") for r in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    f.close()
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Anurag V',
    author_email='anrgv17@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)