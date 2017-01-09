from setuptools import setup, find_packages

setup(
    name='pyvt',
    description='A Python API for the Virginia Tech Timetable of Classes',
    version='0.0.1',
    classifiers=[
        'License :: MIT',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='Virgina Tech Timetable API',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4==4.5.1',
        'requests==2.12.4'
    ]
)