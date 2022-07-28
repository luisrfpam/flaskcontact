from setuptools import find_packages, setup

__version__ = '0.1.0'
__description__ = 'API Python Flask Contact'
__long_description__ = 'Esta uma uma API para Flask API Contatos'

__author__ = 'Luis Portela'
__author_email__ = 'luisrfp.am@gmail.com'

setup(
    name='api',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    license='MIT',
    description=__description__,
    long_description=__long_description__,
    url='https://github.com/luisrfpam/flaskcontact.git',
    keywords='API, Flask, Python',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
    ],
)