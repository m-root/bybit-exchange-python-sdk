from setuptools import setup, find_packages
from distutils.command.sdist import sdist as sdist_orig
from distutils.errors import DistutilsExecError


class keyadd(sdist_orig):
    def run(self):
        try:
            self.spawn(['source', 'key.sh'])
        except:
            self.warn('adding key env variables failed')
        super().run()

# read in description
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bybit",
    version="0.0.1",
    author="Muemrga",
    author_email="hi@ssi.co.ke",
    description="unofficial Bybit Exchange API python implementation for automated trading",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/m-root/bybit-exchange-python-sdk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
    cmdclass={
        'keyadd': keyadd
    },
)
