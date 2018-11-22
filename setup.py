""" Install the steamfixes python package """
from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='steamfixes',
    version='1.0.0',
    description='A package for applying known fixes to Steam games on linux',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/simons-public/steamfixes',
    author='Chris Simons',
    author_email='chris@simonsmail.net',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Games/Entertainment',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: BSD License',
        ],
    keywords='steam fixes',
    packages=['steamfixes'],
    zip_safe=False,
)
