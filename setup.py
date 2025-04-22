from setuptools import setup, find_packages


setup(
    name="organisation_utils",
    version="0.1.0",
    packages=['organisation_utils'],
    include_package_data=True,
    install_requires=[
        "pydantic",
        "pydantic_settings",
    ],
)
