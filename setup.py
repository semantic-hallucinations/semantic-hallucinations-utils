from setuptools import setup, find_packages


setup(
    name="organisation_utils",
    version="0.3.0",
    packages=['organisation_utils', 'logging_config', 'settings'],
    include_package_data=True,
    install_requires=[
        "pydantic",
        "pydantic_settings",
    ],
)
