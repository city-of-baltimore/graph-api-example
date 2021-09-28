"""Setup script for msgraph_example package."""
import os

from setuptools import find_packages
from setuptools import setup


setup(
    name="msgraph_example",  # update this to reflect your project name
    version="0.1.0",
    description="Connect to the Microsoft Graph API using msgraph-core",
    author="City of Baltimore",
    install_requires=[
        "dynaconf",
        "msgraph-core",
        "azure-identity",
    ],
    include_package_data=True,
    package_dir={"": "src"},  # this is required to access code in src/
    packages=find_packages(where="src"),  # same as above
)
