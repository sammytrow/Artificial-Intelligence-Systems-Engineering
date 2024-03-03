class validator():

#User vals

    def checkSpecialChars(self, string):
        special_char = False
            for char in string:
                if (not letter.isnumeric() and not letter.isdigit()):
                    special_char = True
                    break
                return special_char

    def valUserID(self, userID):
        if userID is not None:
            if type(userID) == int is True:
                if len(userID) == 6:
                    return True
        else:
            return False

    def valUserName(self, userName):
        if userName is not None:
            x = self.checkSpecialChars(userName)
            if x = False:
                if len(userName) <= 20:
                    return True #Passed
        else:
            return False #Failed

        def valPassword(self, password):
            ""

#Location vals

    def valLocation(self, args):
        for arg in args:
            x = self.checkSpecialChars(arg)
            if x = False:
                if len(arg) >= 20:
                    passes = passes + 1
                else:
                    fails = fails + 1
        if fails = > 0:
            return False #Something failed
        else:
            return True

#Activity vals

    def valOpeningTimes():
        ""

    def valLocation():
        ""

    def valActivity():
        ""

    def valWebsite():
        ""

    def valPrice():
        ""
        

        
        
            
            
