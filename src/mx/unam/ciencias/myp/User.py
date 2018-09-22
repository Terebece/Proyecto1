class User():

    userstatus = ["ACTIVE", "AWAY", "BUSY"]
    salas = []

    def __init__(self, connection, address):
        """
        Constructor que inicializa a un usuario con: su conexión, su dirección,
        su estado, una bandera para saber si el usuario ya se identificó y pueda
        utilizar el chat y el nombre del usuario.
        """
        self.connection = connection
        self.address = address
        self.status = "ACTIVE"
        self.identified = False
        self.name = " "

    def setConn(self, connection):
        """
        Función que define una nueva conexión para el usuario.
        """
        self.connection = connection

    def getConn(self):
        """
        Función que regresa la conexión del usuario.
        """
        return self.connection

    def setAddress(self, address):
        """
        Función que define una nueva dirección para el usuario.
        """
        self.address = address

    def getAddress(self):
        """
        Función que regresa la dirección del usuario.
        """
        return self.address

    def getName(self):
        """
        Función que regresa el nombre del usuario.
        """
        return self.name

    def setName(self, name):
        """
        Función que define un nuevo nombre para el usuario.
        """
        self.name = name
        self.identified = True

    def getIdentified(self):
        """
        Función que nos regresa si el usuario ya se identificó.
        """
        return self.identified

    def getStatus(self):
        """
        Función que regresa el estado del usuario.
        """
        return self.userstatus

    def setStatus(self, status):
        """
        Función que define un nuevo estado para el usuario.
        """
        for s in self.userstatus:
            if s == status:
                self.status = status
