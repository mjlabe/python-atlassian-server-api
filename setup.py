import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-atlassian-server-api-nevermorefu",
    version="0.0.1",
    author="Marc LaBelle",
    author_email="mjlabe@gmail.com",
    description="Communicate with Atlassian's JIRA and BitBucket REST API's",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)