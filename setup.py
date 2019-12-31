import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="azure_utility_tool",
    version="0.0.1",
    author="Miguel Alex Cantu",
    author_email="miguel.can2@gmail.com",
    description="Utility tool for Azure AD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alextricity25/azure_utlity_tool",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
