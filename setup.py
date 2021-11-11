from setuptools import setup, find_packages
import pathlib
import pystego

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='pystego',
    version=pystego.__version__,
    description='Hide secret data within a digital image using good ol\' terminal',
    long_description=README,
    license=pystego.__license__,
    classifiers=[
        f"License :: OSI Approved :: {pystego.__license__}",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    author=pystego.__author__,
    packages=find_packages(exclude=("tests",)),
    install_requires=[
        'numpy',
        'Pillow',
    ],
    entry_points={
        "console_scripts": [
            "pystego = pystego.__main__:main",
        ]
    },
)