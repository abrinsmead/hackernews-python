import os

from setuptools import setup

import hackernews


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='hackernews-python',
    version=hackernews.__version__,
    description='Python wrapper for the official Hacker News API (v0)',
    long_description=(read('README.rst') + '\n' + read('HISTORY.rst')),
    url='https://github.com/abrinsmead/hackernews-python',
    license='MIT',
    author='Alex Brinsmead',
    author_email='alex.brinsmead@dataloft.com',
    py_modules=['hackernews'],
    install_requires=['requests>=2.4.3'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)