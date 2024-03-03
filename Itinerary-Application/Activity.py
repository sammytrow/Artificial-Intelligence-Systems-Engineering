class Activity():
    openingTimes = ""
    location = ""
    activity = ""
    website = ""
    price = ""

    def setValues(self):
        self.openingTimes = setOpeningTimes()
        self.location = setLocation()
        self.activity = setActivity()
        self.website = setWebsite()
        self.price = setPrice()

    def getValues(self):
        values = []
        values.append(getOpeningTimes())
        values.append(getLocation())
        values.append(getActivity())
        values.append(getWebsite())
        values.append(getPrice())

    def setOpeningTimes(self, openingTimes):
        self.openingTimes = openingTimes

    def setLocation(self, location):
        self.location = location

    def setActivity(self, activity):
        self.activity = activity

    def setWebsite(self, website):
        self.website = website

    def setPrice(self, price):
        self.price = price

    def getOpeningTimes(self):
        return self.openingTimes

    def getLocation(self):
        return self.location

    def getActivity(self):
        return self.activity

    def getWebsite(self):
        return self.website

    def getPrice(self):
        return self.price