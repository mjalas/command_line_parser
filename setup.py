from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
#long_description = ""

#try:
#    from pypandoc import convert
#    if path.exists(path.join(here, 'README.md')):
#        long_description = convert('README.md', 'rst')
#except ImportError:
#    print("warning: pypandoc module not found, could not convert Markdown to RST")

setup(
    name='command-line-parser',
    version='0.0.3',
    description='A customizable command line parser',
    #long_description=long_description,
    url='https://github.com/mjalas/command-line-parser',
    author='Mats Jalas',
    author_email='mats.jalas@gmail.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='command-line-parsing argument-parsingoption-parsing',
    setup_requires=['nose>=1.0', 'coverage>=4.0.3', 'pypandoc>=1.1.3'],
    packages=find_packages(exclude=['tests'])
)
