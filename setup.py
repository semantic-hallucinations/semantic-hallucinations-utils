from setuptools import setup, find_packages


setup(
    name="organisation_utils",
    version="0.3.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pydantic",
        "pydantic_settings",
    ],
)
