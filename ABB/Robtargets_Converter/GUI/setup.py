from setuptools import setup, find_packages
setup(
    name="ABB_RapidTools",
    version="0.1",
    packages=find_packages(),
    scripts=['ABB_RapidTools.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    #install_requires=['docutils>=0.3'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.xml'],

    },

    # metadata for upload to PyPI
    author="Xabier Fernandez Gutierrez",
    author_email="xabier.fernandez@outlook.com",
    description="Program to manipulate ABB files",
    license="GPL 3.0",
    keywords="abb rapid tools",
    url="https://github.com/XabierFernandez",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)