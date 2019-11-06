from setuptools import setup
from postmancli.metadata import Metadata
from io import open

metadata = Metadata()
with open("README.md", "r", encoding="utf-8") as md_file:
    long_description = md_file.read()


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list


setup(
    name='postmancli',
    packages=['postmancli'],
    install_requires=requirements(),
    version=metadata.get_version(),
    license='LGPL v3',
    description='CLI tool for emails sending using SMTP server',
    long_description_content_type="text/markdown",
    long_description=long_description,
    author=metadata.get_author(),
    author_email='contact@rdch106.hol.es',
    url='https://github.com/RDCH106/postman-cli',
    download_url='https://github.com/RDCH106/postman-cli/archive/v'+metadata.get_version()+'.tar.gz',
    entry_points={
        'console_scripts': ['postmancli=postmancli.main:main'],
    },
    keywords='cli command-line email-sender',
    classifiers=['Programming Language :: Python',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8'],
)
