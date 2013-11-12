import os

from setuptools import find_packages
from setuptools import setup

project = 'kotti_settings'
version = '0.2'

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

tests_require = [
    'wsgi_intercept==0.5.1',
]

setup(
    name=project,
    version=version,
    description="Settings configuration for Kotti",
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Pylons",
        "Framework :: Pyramid",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: User Interfaces",
    ],
    keywords='kotti ui settings cms pyramid pylons',
    author='Marco Scheidhuber',
    author_email='j23d@jusid.de',
    url='https://github.com/j23d/kotti_settings',
    license='BSD-derived (http://www.repoze.org/LICENSE.txt)',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    tests_require=[
        tests_require,
    ],
    install_requires=[
        'Kotti>=0.9b2',
        'pyramid_deform<=0.2',
    ],
    extras_require={
        'testing': tests_require,
    },
    message_extractors={
        'kotti_settings': [
            ('**.py', 'lingua_python', None),
            ('**.zcml', 'lingua_xml', None),
            ('**.pt', 'lingua_xml', None),
        ]
    },
)
