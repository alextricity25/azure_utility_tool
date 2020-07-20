
class TestCases():

    def __init__(self):
        self.name = "TestCases"

    def get_test_user_graph_data(self):
        """
        This is what the get user graph API call returns as of 12/28/2019
        """
        data = {'@odata.context': 'https://graph.microsoft.com/v1.0/$metadata#users(userPrincipalName,displayName,mail,city,state,postalCode,country,usageLocation,department,jobTitle,officeLocation,onPremisesExtensionAttributes,userType,isResourceAccount,id)',
 'value': [{'city': 'Olathe',
            'country': 'USA',
            'department': 'Accounting',
            'displayName': 'randomacc057',
            'id': '8d2be0b3-5815-4234-b1c4-db8be9388def',
            'isResourceAccount': None,
            'jobTitle': 'A/P Supervisor',
            'mail': 'randomacc057@kc.company.com',
            'officeLocation': None,
            'onPremisesExtensionAttributes': {'extensionAttribute1': None,
                                              'extensionAttribute10': None,
                                              'extensionAttribute11': None,
                                              'extensionAttribute12': None,
                                              'extensionAttribute13': None,
                                              'extensionAttribute14': None,
                                              'extensionAttribute15': None,
                                              'extensionAttribute2': None,
                                              'extensionAttribute3': None,
                                              'extensionAttribute4': None,
                                              'extensionAttribute5': None,
                                              'extensionAttribute6': None,
                                              'extensionAttribute7': '111',
                                              'extensionAttribute8': None,
                                              'extensionAttribute9': None},
            'postalCode': '000000',
            'state': 'Kansas',
            'usageLocation': 'GB',
            'userPrincipalName': 'lukeskywalker@kc.company.com',
            'userType': None},
           {'city': None,
            'country': None,
            'department': None,
            'displayName': 'Darth Vader',
            'id': 'ff9d07bf-ddb6-4f31-bed0-f74934b656d7',
            'isResourceAccount': None,
            'jobTitle': None,
            'mail': 'vader@corp.company.com',
            'officeLocation': None,
            'onPremisesExtensionAttributes': {'extensionAttribute1': None,
                                              'extensionAttribute10': None,
                                              'extensionAttribute11': None,
                                              'extensionAttribute12': None,
                                              'extensionAttribute13': None,
                                              'extensionAttribute14': None,
                                              'extensionAttribute15': None,
                                              'extensionAttribute2': None,
                                              'extensionAttribute3': None,
                                              'extensionAttribute4': None,
                                              'extensionAttribute5': None,
                                              'extensionAttribute6': None,
                                              'extensionAttribute7': '000',
                                              'extensionAttribute8': None,
                                              'extensionAttribute9': None},
            'postalCode': None,
            'state': None,
            'usageLocation': 'US',
            'userPrincipalName': 'darth_vader@company.com',
            'userType': 'Member'},
           {'city': None,
            'country': None,
            'department': None,
            'displayName': 'Akbar',
            'id': 'f33bf278-97b6-4576-bc2a-d0835aba7620',
            'isResourceAccount': None,
            'jobTitle': None,
            'mail': 'akbar@corp.company.com',
            'officeLocation': None,
            'onPremisesExtensionAttributes': {'extensionAttribute1': None,
                                              'extensionAttribute10': None,
                                              'extensionAttribute11': None,
                                              'extensionAttribute12': None,
                                              'extensionAttribute13': None,
                                              'extensionAttribute14': None,
                                              'extensionAttribute15': None,
                                              'extensionAttribute2': None,
                                              'extensionAttribute3': None,
                                              'extensionAttribute4': None,
                                              'extensionAttribute5': None,
                                              'extensionAttribute6': None,
                                              'extensionAttribute7': '000',
                                              'extensionAttribute8': None,
                                              'extensionAttribute9': None},
            'postalCode': None,
            'state': None,
            'usageLocation': 'US',
            'userPrincipalName': 'akbar@corp.company.com',
            'userType': 'Member'}]}

        return data

    def get_test_user_reg_info_graph_data(self):
        data = {
            '@odata.context': 'https://graph.microsoft.com/beta/$metadata#reports/credentialUserRegistrationDetails',
            'value': [
                {'authMethods': ['officePhone', 'appNotification', 'appCode'],
                 'id': '8d2be0b3-5815-4234-b1c4-db8be9388def',
                 'isCapable': False,
                 'isEnabled': True,
                 'isMfaRegistered': False,
                 'isRegistered': False,
                 'userDisplayName': 'Willow, Solomon',
                 'userPrincipalName': '000-darth_vader@company.com'},
                {'authMethods': ['appNotification', 'appCode'],
                 'id': 'ff9d07bf-ddb6-4f38-bed0-f74934b656d7',
                 'isCapable': False,
                 'isEnabled': True,
                 'isMfaRegistered': False,
                 'isRegistered': False,
                 'userDisplayName': 'Akbar',
                 'userPrincipalName': 'akbar@corp.company.com'},
                {'authMethods': ['officePhone'],
                 'id': 'f33bf278-97b6-4576-bc2a-d0835aba7620',
                 'isCapable': False,
                 'isEnabled': True,
                 'isMfaRegistered': False,
                 'isRegistered': False,
                 'userDisplayName': 'Han',
                 'userPrincipalName': 'han@corp.company.com'},
                {'authMethods': [],
                 'id': 'a075e7b0-bb19-4a4e-98e0-409f542eeea0',
                 'isCapable': False,
                 'isEnabled': True,
                 'isMfaRegistered': False,
                 'isRegistered': False,
                 'userDisplayName': 'Threepio',
                 'userPrincipalName': 'threepio@corp.company.com'},
                {'authMethods': [],
                 'id': '476d141e-c8da-4459-9517-9c5fcb22363d',
                 'isCapable': False,
                 'isEnabled': True,
                 'isMfaRegistered': False,
                 'isRegistered': False,
                 'userDisplayName': 'Artoo',
                 'userPrincipalName': 'Artoo@corp.company.com'}]}

        return data

    def get_users_in_enforced_groups_test_data(self):
        data = {'@odata.context': 'https://graph.microsoft.com/v1.0/$metadata#directoryObjects',
 'value': [{'@odata.type': '#microsoft.graph.user',
            'businessPhones': ['555'],
            'displayName': 'Bear, Rey',
            'givenName': 'Rey',
            'id': '60112a02-4135-4794-b66d-764f3ce7cea7',
            'jobTitle': 'HR Business Partner',
            'mail': 'rey.bear@company.com',
            'mobilePhone': None,
            'officeLocation': None,
            'preferredLanguage': None,
            'surname': 'Bearden',
            'userPrincipalName': 'rbear@company.com'},
           {'@odata.type': '#microsoft.graph.user',
            'businessPhones': ['555'],
            'displayName': 'Pam',
            'givenName': 'Pam',
            'id': '53e21b03-4ae8-4db7-88f0-c8cb9d8ee2a9',
            'jobTitle': 'Finance Analyst',
            'mail': 'pam@company.com',
            'mobilePhone': '555',
            'officeLocation': 'rainbows',
            'preferredLanguage': None,
            'surname': 'blah',
            'userPrincipalName': 'pbalh34@company.com'},
           {'@odata.type': '#microsoft.graph.user',
            'businessPhones': ['555'],
            'displayName': 'Johnston, Steve',
            'givenName': 'Steve',
            'id': '17e18d09-5e13-47b4-885d-e11f2ff6b133',
            'jobTitle': 'Vice\xa0President,\xa0Company - Market\xa0President',
            'mail': 'johnston.steve@corp.company.com',
            'mobilePhone': '555',
            'officeLocation': 'Remote Corp Employee',
            'preferredLanguage': None,
            'surname': 'Johnston',
            'userPrincipalName': 'ddff423@corp.company.com'},
           {'@odata.type': '#microsoft.graph.user',
            'businessPhones': ['555'],
            'displayName': 'Maria Susan',
            'givenName': 'Maria',
            'id': '7f91e90b-7378-446a-80ff-45eeaa27a0a0',
            'jobTitle': 'A/R Coordinator',
            'mail': 'maria.susan@company.com',
            'mobilePhone': None,
            'officeLocation': 'clouds',
            'preferredLanguage': None,
            'surname': 'Susan',
            'userPrincipalName': 'msus32@company.com'},
           {'@odata.type': '#microsoft.graph.user',
            'businessPhones': ['555'],
            'displayName': 'Jack Paul',
            'givenName': 'Jack',
            'id': '8d2be0b3-5815-4234-b1c4-db8be9388def',
            'jobTitle': 'Finance Manager',
            'mail': 'jack.paul@company.com',
            'mobilePhone': None,
            'officeLocation': 'Tatooine',
            'preferredLanguage': None,
            'surname': 'Paul',
            'userPrincipalName': 'jpau345@wcf.company.com'}]}

        return data

    def get_group_test_data(self):
        data = {
            "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#groups/$entity",
            "createdDateTime": "2011-07-26T23:48:51Z",
            "creationOptions": [],
            "displayName": "Clone Troopers",
            "groupTypes": [],
            "id": "baavc5f30-f44b-4903-8237-cb630b1690ce",
            "mail": "Clone-Troopers@firstorder.com",
            "mailNickname": "CTBoss",
            "onPremisesDomainName": "firstorder.com",
            "onPremisesLastSyncDateTime": "2023-03-19T22:16:21Z",
            "onPremisesNetBiosName": "NA",
            "onPremisesProvisioningErrors": [],
            "onPremisesSamAccountName": "Clone-Troopers",
            "onPremisesSecurityIdentifier": "S-1-5-21-1645522239-879982540-1417001233-605714",
            "proxyAddresses": [
            "SMTP:Clone-Troopers@firstorder.com"
            ],
            "renewedDateTime": "2012-07-26T23:48:51Z",
            "resourceBehaviorOptions": [],
            "resourceProvisioningOptions": [],
            "securityIdentifier": "S-1-12-1-3133127136-1221695915-1674307470-3465549323",
            }
        return data

    def get_application_test_data(self):
        data = {
            "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#applications",
            "value": [
                {
                    "addIns": [],
                    "api": {
                        "acceptMappedClaims": None,
                        "knownClientApplications": [],
                        "oauth2PermissionScopes": [
                            {
                                "adminConsentDescription": "Allow the application to access TestApp OnDemand on behalf of the signed-in user.",
                                "adminConsentDisplayName": "Access TestApp OnDemand",
                                "id": "asdf356c8-8b99-480c-be07-a21a1cd35ef6",
                                "isEnabled": True,
                                "type": "User",
                                "userConsentDescription": "Allow the application to access TestApp OnDemand on your behalf.",
                                "userConsentDisplayName": "Access TestApp OnDemand",
                                "value": "user_impersonation"
                            }
                        ],
                        "preAuthorizedApplications": [],
                        "requestedAccessTokenVersion": None
                    },
                    "appId": "480e1db5-6da4-46e3-8fd5-48f2d9a0f171",
                    "appRoles": [
                        {
                            "allowedMemberTypes": [
                                "User"
                            ],
                            "description": "msiam_access",
                            "displayName": "msiam_access",
                            "id": "b9632174-c057-4dfe-951b-be3adc52bfe6",
                            "isEnabled": True,
                            "origin": "Application",
                            "value": None
                        },
                        {
                            "allowedMemberTypes": [
                                "User"
                            ],
                            "description": "User",
                            "displayName": "User",
                            "id": "18d14569-asdf-439b-9a66-3a2aee01d14f",
                            "isEnabled": True,
                            "origin": "Application",
                            "value": None
                        }
                    ],
                    "applicationTemplateId": None,
                    "createdDateTime": "2016-08-10T22:24:57Z",
                    "deletedDateTime": None,
                    "displayName": "TestApp OnDemand",
                    "groupMembershipClaims": None,
                    "id": "015b2bd3-80b6-4faf-asdf-914ec398d125",
                    "identifierUris": [
                        "https://blah",
                        "http://cadfaiosdf",
                    ],
                    "info": {
                        "logoUrl": "https://blah",
                        "marketingUrl": None,
                        "privacyStatementUrl": None,
                        "supportUrl": None,
                        "termsOfServiceUrl": None
                    },
                    "isDeviceOnlyAuthSupported": None,
                    "isFallbackPublicClient": False,
                    "keyCredentials": [],
                    "optionalClaims": None,
                    "parentalControlSettings": {
                        "countriesBlockedForMinors": [],
                        "legalAgeGroupRule": "Allow"
                    },
                    "passwordCredentials": [],
                    "publicClient": {
                        "redirectUris": []
                    },
                    "publisherDomain": None,
                    "requiredResourceAccess": [],
                    "signInAudience": "AzureADMyOrg",
                    "spa": {
                        "redirectUris": []
                    },
                    "tags": [],
                    "tokenEncryptionKeyId": None,
                    "web": {
                        "homePageUrl": "https://127.0.0.1:444/applications/default.aspx?metadata=customappsso|ISV9.1|primary|z",
                        "implicitGrantSettings": {
                            "enableAccessTokenIssuance": False,
                            "enableIdTokenIssuance": True
                        },
                        "logoutUrl": None,
                        "redirectUris": [
                            "https://blah",
                            "https://127.0.0.1:444/applications/default.aspx"
                        ]
                    }
                },
                {
                    "addIns": [],
                    "api": {
                        "acceptMappedClaims": None,
                        "knownClientApplications": [],
                        "oauth2PermissionScopes": [
                            {
                                "adminConsentDescription": "Allow the application to access TestApp2 on behalf of the signed-in user.",
                                "adminConsentDisplayName": "Access TestApp2",
                                "id": "96vejje5-d9c1-4f0b-9754-5bc6fd7b6b72",
                                "isEnabled": True,
                                "type": "User",
                                "userConsentDescription": "Allow the application to access TestApp2 on your behalf.",
                                "userConsentDisplayName": "Access TestApp2",
                                "value": "user_impersonation"
                            }
                        ],
                        "preAuthorizedApplications": [],
                        "requestedAccessTokenVersion": None
                    },
                    "appId": "b218ce2c-5ea2-4e02-bcdc-0cacd088e22a",
                    "appRoles": [
                        {
                            "allowedMemberTypes": [
                                "User"
                            ],
                            "description": "User",
                            "displayName": "User",
                            "id": "18ddff69-c3bd-439b-9a66-3a2aee01d14f",
                            "isEnabled": True,
                            "origin": "Application",
                            "value": None
                        },
                        {
                            "allowedMemberTypes": [
                                "User"
                            ],
                            "description": "msiam_access",
                            "displayName": "msiam_access",
                            "id": "b96asdf74-c057-4f7e-951b-be3adc52bfe6",
                            "isEnabled": True,
                            "origin": "Application",
                            "value": None
                        }
                    ],
                    "applicationTemplateId": None,
                    "createdDateTime": "2019-02-28T19:24:29Z",
                    "deletedDateTime": None,
                    "displayName": "TestApp2",
                    "groupMembershipClaims": None,
                    "id": "015adfe-79f3-44fe-bc68-e2a852532ee4",
                    "identifierUris": [
                        "blah2"
                    ],
                    "info": {
                        "logoUrl": None,
                        "marketingUrl": None,
                        "privacyStatementUrl": None,
                        "supportUrl": None,
                        "termsOfServiceUrl": None
                    },
                    "isDeviceOnlyAuthSupported": None,
                    "isFallbackPublicClient": False,
                    "keyCredentials": [],
                    "optionalClaims": None,
                    "parentalControlSettings": {
                        "countriesBlockedForMinors": [],
                        "legalAgeGroupRule": "Allow"
                    },
                    "passwordCredentials": [],
                    "publicClient": {
                        "redirectUris": []
                    },
                    "publisherDomain": "Sysco.onmicrosoft.com",
                    "requiredResourceAccess": [],
                    "signInAudience": "AzureADMyOrg",
                    "spa": {
                        "redirectUris": []
                    },
                    "tags": [],
                    "tokenEncryptionKeyId": None,
                    "web": {
                        "homePageUrl": "https://account.activedirectory.windowsazure.com:444/applications/default.aspx?metadata=customappsso|ISV9.1|primary|z",
                        "implicitGrantSettings": {
                            "enableAccessTokenIssuance": False,
                            "enableIdTokenIssuance": True
                        },
                        "logoutUrl": None,
                        "redirectUris": [
                            "blash",
                            "blasdfi"
                        ]}}]}
        return data
