class User():

    userstatus = ["ACTIVE", "AWAY", "BUSY"]
    salas = []

    def __init__(self, connection, address):
        """
        Constructor que inicializa a un usuario con: su conexion, su direccion,
        su estado, una bandera para saber si el usuario ya se identifico y pueda
        utilizar el chat y el nombre del usuario.
        """
        self.connection = connection
        self.address = address
        self.status = "ACTIVE"
        self.identified = False
        self.name = " "

    def setConn(self, connection):
        """
        Metodo que define una nueva conexion para el usuario.
        """
        self.connection = connection

    def getConn(self):
        """
        Metodo que regresa la conexion del usuario.
        """
        return self.connection

    def setAddress(self, address):
        """
        Metodo que define una nueva direccion para el usuario.
        """
        self.address = address

    def getAddress(self):
        """
        Metodo que regresa la direccion del usuarioself.
        """
        return self.address

    def getName(self):
        """
        Metodo que regresa el nombre del Usuario.
        """
        return self.name

    def setName(self, name):
        """
        Metodo que define un nuevo nombre para el usuario.
        """
        self.name = name
        self.identified = True

    def getIdentified(self):
        """
        Metodo que nos regresa si el usuario ya se identifico.
        """
        return self.identified

    def getStatus(self):
        """
        Metodo que regresa el estado del usuario.
        """
        return self.userstatus

    def setStatus(self, status):
        """
        Metodo que define un nuevo estado para el usuario.
        """
        for s in self.userstatus:
            if s == status:
                self.status = status
