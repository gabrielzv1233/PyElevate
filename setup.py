from setuptools import setup, find_packages

setup(
    name="PyElevate",
    version="0.1.0",
    author="Gabrielzv1233",
    author_email="gabrielzv1233@gmail.com",
    url="https://github.com/gabrielzv1233/PyElevate",
    license="MIT",
    description="Python library for requesting root privileges",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pyelevate = PyElevate.__init__:main",
        ]
    },
)
