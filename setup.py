from setuptools import setup
from define_cli import __version__ as VERSION

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as file:
    requires = [line.strip() for line in file.readlines()]

DESCRIPTION = "Definitions of words from Dictionary are now in your terminal, with rich output."

setup(
    name="def-cli",
    version=VERSION,
    url="https://github.com/ghostofpokemon/define-cli",
    project_urls={
        "Changelog": "https://github.com/ghostofpokemon/define-cli/releases",
        "Source": "https://github.com/ghostofpokemon/define-cli",
    },
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ghostofpokemon",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Utilities",
    ],
    packages=["define_cli"],
    install_requires=requires,
    include_package_data=True,
    package_data={"define_cli": ["define_cli/*"]},
    python_requires=">=3.5",
    entry_points={"console_scripts": ["def = define_cli.__main__:cli"]},
)
