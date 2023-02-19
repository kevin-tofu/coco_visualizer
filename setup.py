from setuptools import setup, find_packages
from typing import List
import pathlib
import os
# print(pathlib.Path(__file__).parent)


print(find_packages())

def get_install_requires() -> List[str]:
    """Returns requirements.txt parsed to a list"""
    fpath = f"{pathlib.Path(__file__).parent}/requirements.txt"
    targets = []
    print(fpath)
    if os.path.exists(fpath):
        with open(fpath, 'r') as f:
            targets = f.read().splitlines()
    return targets

setup(
    name='coco_formatter',\
    version="v0.0.1",\
    url='https://github.com/kevin-tofu/coco_formatter',\
    download_url='https://github.com/kevin-tofu/coco_formatter/releases/tag/v0.0.1',\
    description="",\
    install_requires=get_install_requires(),
    # install_requires=['numpy', 'wheel'],
    packages=['coco_formatter'],\
    # packages=find_packages(), \
    package_dir = {'coco_formatter': 'coco_formatter'},\
    author='kevin-tofu',\
    license='Apache-2.0 license', \
    python_requires='>3.8'
)
