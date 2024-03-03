class Itinerary():
    desiredLocation = []
    desiredActivity = ""

    def setDLocation(self, Dlocation):
        self.desiredLocation = Dlocation

    def setDActivity(self, DActivity):
        self.desiredActivity = DActivity

    def getDLocation(self):
        return self.desiredLocation

    def getDActivity(self):
        return self.desiredActivity

    def clearAll(self):
        self.desiredLocation = None

    def addItem(self, item):
        self.desiredLocation.append(item)

    def removeItem(self, item):
        self.desiredLocation.remove(item)
        

    