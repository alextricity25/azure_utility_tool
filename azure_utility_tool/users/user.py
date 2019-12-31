import json

class User():

    def __init__(self,
                 userPrincipalName,
                 displayName,
                 mail,
                 city,
                 state,
                 postalCode,
                 country,
                 usageLocation,
                 department,
                 jobTitle,
                 officeLocation,
                 onPremisesExtensionAttributes,
                 userType,
                 isResourceAccount,
                 id):
        self.userPrincipalName = userPrincipalName
        self.displayName = displayName
        self.mail = mail
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.country = country
        self.usageLocation = usageLocation
        self.department = department
        self.jobTitle = jobTitle
        self.officeLocation = officeLocation
        self.onPremisesExtensionAttributes = onPremisesExtensionAttributes
        self.userType = userTyp
        self.isResourceAccount = isResourceAccount
        self.id = id

