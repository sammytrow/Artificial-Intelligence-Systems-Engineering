class Location():
    street = ""
    postcode = ""
    distance = ""
    cityTown = ""
    country = ""

    def getValues(self):
        values = []
        values.append(getStreet())
        values.append(getPostcode())
        values.append(getDistance())
        values.append(getCityTown())
        values.append(getCountry())
        return values

    def setValues(self):
        setStreet()
        setPostcode()
        setDistance()
        setCityTown()
        setCountry()

    def getStreet(self):
        return self.street

    def getPostcode(self):
        return self.postcode

    def getDistance(self):
        return self.distance

    def getCityTown(self):
        return self.city/town

    def getCountry(self):
        return self.country

    def setStreet(self, street):
        self.street = street

    def setPostcode(self, postcode):
        self.postcode = postcode

    def setDistance(self, distance):
        self.distance = distance

    def setCityTown(self, cityTown):
        self.cityTown = cityTown

    def setCountry(self, country):
        self.country = country