from setuptools import setup

setup(
    name = 'testtest',
    version = '1.0.0',
    install_requires = [
    ],
    entry_points = {
        'console_scripts': [
            'torch = torch:cli',
        ],
    },
)
