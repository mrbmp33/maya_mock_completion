from setuptools import setup, find_packages

with open("./README.md") as f:
    long_description = f.read()
    
setup(
    name="maya_mock_completion",
    version="0.2.0",
    description="A mock version of the Autodesk maya libraries to run code intended for maya using a regular Python interpreter"
                "from a virtual environment.",
    package_dir={
        "": ".",
    },
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrbmp33/maya_mock_completion",
    author="Bernat Mas Pastor",
    author_email="bmp33@duck.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    install_requires=["cmdx >= 0.6.4"],
    extras_require={
        "dev": "twine>=4.0.2",
    },
    python_requires=">=3.10"
)
