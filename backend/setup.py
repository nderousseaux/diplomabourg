import os

from setuptools import setup, find_packages


requires = [] #Dans requirements.in

tests_require = [] #Dans requirements.dev

setup(
    name='hapi',
    version='0.0',
    description='hapi',
    long_description="hapi",
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = hapi:main'
        ],
        'console_scripts': [
            'initialize_db=hapi.utils.db:main',
            'fill_db=hapi.utils.db:fill',
        	'server_start=hapi.server_start:main',
	    ],
    },
)
