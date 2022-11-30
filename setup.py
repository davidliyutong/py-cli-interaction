import os
from setuptools import setup

requires = open("./requirements.txt","r").readlines() if os.path.exists("./requirements.txt") else open("./py_cli_interaction.egg-info/requires.txt","r").readlines()

setup(name="py-cli-interaction",
      version="0.2",
      author="davidliyutong",
      keywords=["python", "CLI", "interaction"],
      author_email="davidliyutong@sjtu.edu.cn",
      description="A library for CLI interaction",
      long_description=open('README.md').read(),
      license="MIT Licence",
      packages=["py_cli_interaction"],
      python_requires=">=3.7",
      install_requires=requires,
      long_description_content_type="text/markdown")