from distutils.core import setup
from setuptools import find_namespace_packages
import django_heartbeat

setup(
    name='django-heartbeat',
    version=django_heartbeat.__version__,
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
