# Azure Utility Tool

The Azure Utility Tool provides a set of utility functions for gathering
useful information from an Azure AD tenant.

# Getting Started with AUT

* Clone the repository
```sh
$ git clone <repo-url>
```
* Install dependencies in virutal environment
```sh
$ cd azure_utility_tool
$ virtualenv -p $(which python3.6) venv
$ . ./venv/bin/activate
$ pip install msal
```
* Install AUT in develop mode
```sh
$ pip install -e
```
* Run the program
```sh
$ cd azure_utility_tool
$ python main.py -h
```
