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
$ pip install -r requirements.txt
```
* Install AUT in develop mode
```sh
$ pip install -e
```
* Create the directories needed with correct permissions

When the CSV output feature is used, AUT creates reports in `/mfa_reports/csv/`
You must ensure this directory exists with proper permissions
```sh
$ mkdir -p /mfa_reports/csv
```
* Configure the program

AUT needs a valid client application registration in an Azure directory before it can run.
The client requires a certificate, as this is the only form of authentication that it supports.
Once you have created a certificate (self-signed is fine), then upload it to the Azure application
registration. Take note of the client_id, tenant ID, and thumbprint. You will also need the private
key file that goes along with the certificate.
To configure AUT, create a file called `aut_config.json` in the `.aut` directory. The `.aut`
directory must reside in the user's home directory i.e. `~/.aut/aut_config.json`.
The `aut_config.json` must be in the following format:
```json
{
	"authority": "https://login.microsoftonline.com/<your-tenant-id>",
	"client_id": "<your-client-id>,
	"scope" ["https://graph.microsoft.com/.default"],
	"thumbprint": "<your-thumprint>",
	"private_key_file": "<full-path-to-private-key>",
	"MFA_ENFORCED_GROUPS": [],
	"MAX_RETRIES": 5,
	"filters": {}
}
```
* Run the program with the help flag
```sh
$ cd azure_utility_tool
$ python main.py -h
```

# Pulling user attributes and SSPR/MFA information
To generate a CSV report with all of the user's in your tenant, plus their SSPR/MFA information,
then run the program with the following arguments:
```sh
$ python main.py list_all_users_mfa -o csv
```
This will generate a report in `/mfa_reports/csv` called `list_all_users_mfa_<date>.csv`
