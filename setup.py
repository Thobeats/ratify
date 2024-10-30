from setuptools import setup, find_packages

# Read the README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ratify',
    packages=find_packages(),
    version='0.3.0',
    description='A simple validation library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='tobiy23@gmail.com',
    python_requires='>=3.6',
    url='https://github.com/Thobeats/ratify',
    install_requires=[
        're',
        'datetime',
        'jsonschema'
    ],
    project_urls={
        "Documentation": "https://iyanu.com.ng/ratify",  # Add your documentation site URL
    },
)
