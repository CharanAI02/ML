from setuptools import find_packages,setup

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str):
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='Regressionproject',
    version='0.0.1',
    author='charan',
    author_email="charan99949@gmail.com",
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()
)