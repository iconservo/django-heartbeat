from distutils.core import setup
from setuptools import find_namespace_packages

setup(
    name='django-heartbeat',
    version='0.0.1',
    packages=find_namespace_packages(),
    url='https://bitbucket.org/redfunction/django-heartbeat',
    license='MIT',
    author='Margus Laak',
    author_email='margus.laak@redfunction.ee',
    description='A single api endpoint to display django system status',
    install_requires=[
        'django>=2.2,<2.3',
        'djangorestframework',
    ]
)
