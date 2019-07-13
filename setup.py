from setuptools import setup, find_packages

exec(open('mvgavg/version.py').read()) # loads __version__

setup(name='mvgavg',
      version=__version__,
      author='NGeorgescu',
    description='Moving averages',
    long_description=open('README.rst').read(),
    license='see LICENSE.txt',
    keywords="mvgavg moving average movingaverage numpy python binning binned running run",
    packages= find_packages())

