class Room():

    def __init__(self, roomname, creator):
        """Constructor que inicializa una sala con: su nombre, el cliente que lo
        creo, una lista de los clientes que fueron invitados y una lista de los
        clientes que aceptaron la invitación a la sala."""
        self.roomname = roomname
        self.creator = creator
        self.guestUser = []
        self.userInRoom = []

    def getRoomName(self):
        """
        Función que regresa el nombre de la sala.
        """
        return self.roomname

    def setRoomName(self, roomname):
        """
        Función que cambia el nombre de la sala.
        """
        self.roomname = roomname

    def getGuestUser(self):
        """
        Función que regresa la lista de los clientes invitados a la sala.
        """
        return self.guestUser

    def getUsersInRoom(self):
        """
        Función que regresa la lista de los clientes en la sala.
        """
        return self.userInRoom

    def addGuestUsers(self, creator, inv):
        """
        Función que agrega a los clientes invitados por el creador a la lista
        de invitados.
        """
        if creator == self.creator:
            self.guestUser.extend(inv)
        else:
            print("No tienes permiso para invitar personas a esta sala.")

    def addUsersInRoom(self, user):
        """
        Función que agrega a los clientes que aceptaron la invitación para unirse
        a la sala.
        """
        self.userInRoom.append(user)

    def msgInRoom(self, client, msg):
        """
        Función para enviar mensajes en la sala.
        """
        for user in self.userInRoom:
            if user != client:
                user.getConn().append(msg.encode("utf8"))
