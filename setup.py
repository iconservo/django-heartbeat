from distutils.core import setup
from setuptools import find_namespace_packages

setup(
    name='django-heartbeat',
    version='0.0.1',
    packages=find_namespace_packages(),
    url='https://github.com/iconservo/django-heartbeat/',
    license='MIT',
    author='IoT Developers @ The Scotts Company',
    author_email='iot-dev@scotts.com',
    description='A single api endpoint to display django system status',
    install_requires=[
        'django>=2.2,<2.3',
        'djangorestframework',
    ]
)
