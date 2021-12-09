#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

REQUIREMENTS_PROD = 'requirements_prod.txt'

def load_requirements(path=REQUIREMENTS_PROD):
    with open(path,"r") as f:
        packages = [line for line in f.read().split('\n') if len(line) > 0]
    return packages

requirements = load_requirements()
test_requirements = ['pytest>=3', ]

setup(
    author="BlueML AI",
    author_email='james.liang.cje@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Machine Learning on the Web.",
    entry_points={
        'console_scripts': [
            'webml=webml.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='webml',
    name='webml',
    packages=find_packages(include=['webml', 'webml.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/BlueML-AI/webml',
    version='0.1.0',
    zip_safe=False,
)
