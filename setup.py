from setuptools import setup, find_packages

setup(
    name="puffercmd",
    version="13.0.0",
    description="no description",
    author="anonymous",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["requests>=2.0.0"],
)
