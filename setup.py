from setuptools import setup, find_packages

with open("readme.md") as f:
    long_description = f.read()
    
setup(
    name="maya_mock_completion",
    version="0.0.1",
    description="A mock version of the Autodesk maya library to run maya code without using mayapy.",
    package_dir={
        "": "maya_mock_completion",
        "maya": "maya",
        "pymel": "pymel",
    },
    packages=find_packages(where="maya_mock_completion") + ["maya", "pymel"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrbmp33/maya_mock_completion",
    author="Bernat Mas Pastor",
    author_email="bmp33@duck.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent"
    ],
    extras_require={
        "dev": "twine>=4.0.2"
    },
    python_requires=">=3.7"
)