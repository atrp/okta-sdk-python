from datetime import datetime

class CustomData:

    types = {
        'lastLogin': datetime
    }

    def __init__(self):

        self.lastLogin = None  # str
