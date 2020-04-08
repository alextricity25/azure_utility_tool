## MICOSOFT GRAPH ENDPOINTS
### Base endpoints
GRAPH_V1_BASE_URL = "https://graph.microsoft.com/v1.0"
GRAPH_BETA_BASE_URL = "https://graph.microsoft.com/beta"

### Retrieve user registration details
### See:
### https://docs.microsoft.com/en-us/graph/api/reportroot-list-credentialuserregistrationdetails?view=graph-rest-beta&tabs=http
USER_REG_DETAILS = (GRAPH_BETA_BASE_URL +
                             "/reports/"
                             "credentialUserRegistrationDetails")
### Retrive attributes for a specific user
### See:
### https://docs.microsoft.com/en-us/graph/api/user-get?view=graph-rest-1.0&tabs=http
ONE_USER_GET = (GRAPH_V1_BASE_URL +
                    "/users"
                    "?$filter=startswith(userPrincipalName, '{}')")

### Retrieve attributes for all users
### See:
### https://docs.microsoft.com/en-us/graph/api/user-get?view=graph-rest-1.0&tabs=http
USER_GET_ENDPOINT = (GRAPH_V1_BASE_URL +
                          "/users"
                          "?$select="
#                          "aboutMe,"
                          "accountEnabled,"
#                          "ageGroup,"
                          #"assignedLicenses,"
#                          "assignedPlans,"
#                          "birthday,"
                           #"businessPhones,"
                           #"city,"
                           "companyName,"
                           "country,"
                           "createdDateTime,"
                           #"department,"
                           "displayName,"
                           #"employeeId,"
#                          "faxNumber,"
                           #"givenName,"
                           #"hireDate,"
                           "id,"
#                          "imAddresses,"
#                          "interests,"
                          #"isResourceAccount,"
                          "jobTitle,"
                          #"lastPasswordChangeDateTime,"
                          #"legalAgeGroupClassification,"
                          #"licenseAssignmentStates,"
                          "mail,"
                          #"mailboxSettings,"
                          #"mailNickname,"
                          #"mobilePhone,"
                          #"mySite,"
                          "officeLocation,"
                          #"onPremisesDistinguishedName,"
                          #"onPremisesDomainName,"
                          "onPremisesExtensionAttributes,"
                          #"onPremisesImmutableId,"
                          #"onPremisesLastSyncDateTime,"
                          #"onPremisesProvisioningErrors,"
                          "onPremisesSamAccountName,"
                          #"onPremisesSecurityIdentifier,"
                          #"onPremisesSyncEnabled,"
                          #"onPremisesUserPrincipalName,"
                          #"otherMails,"
                          #"passwordPolicies,"
#                          "pastProjects,"
                          #"postalCode,"
                          #"preferredDataLocation,"
                          #"preferredLanguage,"
                          #"preferredName,"
                          #"provisionedPlans,"
                          #"proxyAddresses,"
                          #"responsibilities,"
                          #"schools,"
                          #"showInAddressList,"
                          #"skills,"
                          #"signInSessionsValidFromDateTime,"
                          #"state,"
                          #"streetAddress,"
                          #"surname,"
                          "usageLocation,"
                          "userPrincipalName,")
                          #"userType")

### Check Group Membership
### See:
### https://docs.microsoft.com/en-us/graph/api/user-checkmembergroups?view=graph-rest-1.0&tabs=http
### Notes: You must post to this endpoint.
CHECK_MEMBER_GROUPS_ENDPOINT = (GRAPH_V1_BASE_URL +
                                "/{}/"
                                "checkMemberGroups")

### List transitive members
### See:
### https://docs.microsoft.com/en-us/graph/api/group-list-transitivemembers?view=graph-rest-1.0&tabs=http
GROUP_LIST_TRANSITIVEMEMBERS = (GRAPH_V1_BASE_URL +
                                    "/groups/"
                                    "{}/"
                                    "transitiveMembers")

### List directoryAudits
### See:
### https://docs.microsoft.com/en-us/graph/api/directoryaudit-list?view=graph-rest-1.0&tabs=http
DIRECTORYAUDIT_LIST = (GRAPH_V1_BASE_URL +
                         "/auditLogs/"
                         "directoryAudits"
                         "?&$filter=activityDateTime ge {}-{}-{}")

### user:getMemberGroups
### See:
### https://docs.microsoft.com/en-us/graph/api/user-getmembergroups?view=graph-rest-1.0&tabs=http
USER_GETMEMBERGROUPS = (GRAPH_V1_BASE_URL +
                     "/users/"
                     "{}/"
                     "getMemberGroups")

### Get group
### See:
### https://docs.microsoft.com/en-us/graph/api/group-get?view=graph-rest-1.0&tabs=http
GROUP_GET = (GRAPH_V1_BASE_URL +
            "/groups/"
            "{}")
