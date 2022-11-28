
from setuptools import setup

requirements = open("./requirements.txt","r").readlines()

setup(name="py-cli-interaction",
      version="0.1",
      author="davidliyutong",
      keywords=["python", "CLI", "interaction"],
      author_email="davidliyutong@sjtu.edu.cn",
      description="A library for CLI interaction",
      long_description=open('README.md').read(),
      license="MIT Licence",
      packages=["py_cli_interaction"],
      python_requires=">=3.7",
      install_requires=requirements)