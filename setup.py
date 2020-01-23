from setuptools import setup, find_packages


setup(
    name='sfloydapp',
    scripts=['scripts/apptool'],
    package_dir={'app': 'app'},
    packages=find_packages('app/'),
)