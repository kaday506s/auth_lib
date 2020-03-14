from setuptools import setup, find_packages
import ldap_backend

setup(
    name='ldap_lib_backend',
    version=ldap_backend.__version__,
    description=ldap_backend.__description__,
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    test_suite='tests',
)
