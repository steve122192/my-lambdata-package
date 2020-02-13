from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRED = [
    "pandas",
    "sklearn"
]

setup(
    name="lambdata-steve122192-1",
    version="0.1.3",
    author="Steve Reiss",
    author_email="sgreiss92@gmail.com",
    description="functions for assignment",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    install_requires = REQUIRED,
    url="https://github.com/steve122192/my-lambdata-package",
    keywords="lambda school assignment",
    packages=find_packages() # ["lambdata"]
)