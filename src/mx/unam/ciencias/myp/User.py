class User():

    userstatus = ["ACTIVE", "AWAY", "BUSY"]
    salas = []

    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        self.status = "ACTIVE"
        self.identified = False
        self.name = " "

    def setConn(self, connection):
        self.connection = connection

    def getConn(self):
        return self.connection

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
        self.identified = True

    def getIdentified(self):
        return self.identified

    def getStatus(self):
        return self.userstatus

    def setStatus(self, status):
        for s in self.userstatus:
            if s == status:
                self.status = status
