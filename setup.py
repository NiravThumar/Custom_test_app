from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_app_test/__init__.py
from custom_app_test import __version__ as version

setup(
	name="custom_app_test",
	version=version,
	description="test app",
	author="nirav",
	author_email="abc@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
