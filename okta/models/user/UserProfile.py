class UserProfile:

    types = {
        'login': str,
        'email': str,
        'secondEmail': str,
        'firstName': str,
        'lastName': str,
        'mobilePhone': str,
        'ackClosedAccounts': int,
        'ackNewBusiness': int,
        'closeReport': int,
        'lastLogin': str,
        'portalAccessGroup': str,
        'reportGroupList': str
    }

    def __init__(self):

        self.login = None  # str

        self.email = None  # str

        self.secondEmail = None  # str

        self.firstName = None  # str

        self.lastName = None  # str

        self.mobilePhone = None  # str
        
        self.ackClosedAccounts = None  # int
        
        self.ackNewBusiness = None  # int
        
        self.closeReport = None  # int
        
        self.lastLogin = None  # str
        
        self.portalAccessGroup = None  # str
        
        self.reportGroupList = None  # str
