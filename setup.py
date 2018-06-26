from setuptools import setup

setup(
    name='Ride',
    version='2018.6.26',
    py_modules=['ride'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'ride=ride:cli'
        ]
    },
    license='MIT',
)