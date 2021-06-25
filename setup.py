from setuptools import setup, find_packages

setup(
	name="dsa_python", 
	packages=find_packages(where="src"),
	package_dir={'': 'src'}
)
