class Person:
    def __init__(self,s1,s2,s3):
        self.firstName = s1
        self.lastName = s2
        self.eMail = s3
        
    def setFName(self,s1):
        self.firstName = s1
    def setLName(self,s1):
        self.lastName = s1
    def setEMail(self,s1):
        self.eMail = s1
        
    def __gt__(self,other):
        return self.eMail > other.eMail
    def __ge__(self,other):
        return self.eMail >= other.eMail
    def __eq__(self,other):
        return self.email == other.eMail
    def __le__(self,other):
        return self.email <= other.eMail
    def __lt__(self,other):
        return self.eMail < other.eMail
    
    def printOutput(self):
        print("------------------")
        print("Name: ", self.firstName, " ", self.lastName)
        print("Email: ",self.eMail)
    
    def writeOutput(self,file):
        print("writing to file")
        file.write("%s ," %self.firstName)
        file.write("%s ," %self.lastName)
        file.write("%s \n" %self.eMail)