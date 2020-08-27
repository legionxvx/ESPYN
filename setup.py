from subprocess import check_output

from packaging.version import Version
from setuptools import find_packages, setup
from subprocess import CalledProcessError

requirements = []
with open("requirements.txt", "r") as f:
    for line in f:
        line = line.strip()
        if "==" in line:
            requirements.append(line.replace("==", ">="))

excluded_dirs = [
    "*tests*",
]

with open("README.md", "r") as f:
    long_description = f.read()

try:
    version = check_output([
        "git",
        "describe",
        "--tag",
        "--abbrev=0"
    ]).strip()
except (CalledProcessError):
    version = b"0"


# PEP 440
version = str(Version(version.decode("utf-8")))

setup(
    name="espyn",
    version=version,
    author="",
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/legionxvx/espyn",
    packages=find_packages(exclude=excluded_dirs),
    install_requires=requirements,
    python_requires=">=3.7.3",
)
