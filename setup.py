"""Python setup.py for mars_sre_runbook_engine package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("mars_sre_runbook_engine", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="mars_sre_runbook_engine",
    version=read("mars_sre_runbook_engine", "VERSION"),
    description="Awesome mars_sre_runbook_engine created by SamuelWitke",
    url="https://github.com/SamuelWitke/mars-sre-runbook-engine/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="SamuelWitke",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["mars_sre_runbook_engine = mars_sre_runbook_engine.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
