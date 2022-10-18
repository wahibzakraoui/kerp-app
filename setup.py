from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in kerp/__init__.py
from kerp import __version__ as version

setup(
	name="kerp",
	version=version,
	description="Kerp",
	author="Wahib ZAKRAOUI",
	author_email="wahib@techify.ma",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
