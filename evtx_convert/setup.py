import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="evtx_convert",
    version="1.0.0",
    author="Spiros Politis",
    author_email="spiros.politis@gmail.com",
    description="A package for converting Windows Event Log records to different formats.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spirospolitis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)