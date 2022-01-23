import ast
import re

import setuptools

_version_re = re.compile(r"__version__\s+=\s+(.*)")

with open("poolify/__init__.py") as f:
    version = ast.literal_eval(_version_re.search(f.read()).group(1))

with open("README.md", encoding="utf8") as f:
    readme = f.read()

install_requires = []

dev_requires = [
    "pytest",
    "pytest-cov",
    "pytest-benchmark",
    "mock",
    "coverage",
    "tox",
    # flake8 extensions
    "flake8",
    "mccabe",
    "pep8-naming",
    "flake8-bugbear",
    "flake8-commas",
    "flake8-comprehensions",
    "flake8-builtins",
    "flake8-pytest",
    "flake8-mock",
    # test dependencies
    "pymysql",
]

setuptools.setup(
    name="poolify",
    version=version,
    url="https://github.com/Leosocy/poolify",
    project_urls={
        "Code": "https://github.com/Leosocy/poolify",
        "Issue tracker": "https://github.com/Leosocy/poolify/issues",
    },
    license="MIT",
    author="leosocy",
    author_email="leosocy@gmail.com",
    description="A powerful, pluggable and easy-to-use database connection pooling library in Python.",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Database",
        "Topic :: Utilities",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=setuptools.find_packages(exclude=["docs", "tests"]),
    python_requires=">=3.6",
    install_requires=install_requires,
    extras_require={"dev": dev_requires},
)
