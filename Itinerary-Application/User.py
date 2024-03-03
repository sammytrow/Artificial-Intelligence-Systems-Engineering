class User():
    userID = ""
    userName = ""
    password = ""
    currentLocation = ""

    def __init__(self):
        self.setValues()

    def setValues(self):
        self.userID = setUserID()
        self.userName = setUserName()
        self.password = setPassword()
        self.currentLocation = setCurrentLocation()

"""
    def getValues(self):
        values = []
        values.append(getUserID())
        values.append(getUserName())
        values.append(getPassword())
        values.append(getCurrentLocation())
        return values
"""

    def setUserID(self, userID):
        self.userID = userID

    def setUserName(self, userName):
        self.userName = userName

    def setPassword(self, password):
        self.password = password

    def setCurrentLocation(self, currentLocation):
        self.currentLocation = currentLocation

    def getUserID(self):
        return self.userID

    def getUserName(self):
        return self.userName()

    def getPassword(self):
        return self.password

    def getCurrentLocation(self):
        return self.currentLocation

    