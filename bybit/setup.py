import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bybit",
    version="0.0.1",
    author="Muema",
    author_email="hi@ssi.co.ke",
    description="unofficial Bybit Exchange API python implementation for automated trading",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/m-root/bybit-exchange-python-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
)
