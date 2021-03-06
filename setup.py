from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages

setup(
    name='athena',
    version='0.5',
    packages=find_packages('code'),
    package_dir={'': 'code'},    
    py_modules=[splitext(basename(path))[0] for path in glob('code/athena/*.py')],
    url='',
    license='',
    author='Filip Zagorski',
    author_email='',
    description='',
    install_requires=[
        'requests',
        'scipy',
        ]
)
