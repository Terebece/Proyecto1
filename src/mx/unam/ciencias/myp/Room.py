class Room():

    def __init__(self, roomname, creator):
        self.roomname = roomname
        self.creator = creator
        self.guestUser = []
        self.userInRoom = []

    def getRoomName(self):
        return self.roomname

    def setRoomName(self, roomname):
        self.roomname = roomname

    def getGuestUser(self):
        return self.guestUser

    def getUsersInRoom(self):
        return self.userInRoom

    def addGuestUsers(self, creator, inv):
        if creator == self.creator:
            self.guestUser.extend(inv)
        else:
            print("No tienes permiso para invitar personas a esta sala.")

    def addUsersInRoom(self, user):
        self.userInRoom.append(user)

    def msgInRoom(self, client, msg):
        for user in self.userInRoom:
            if user != client:
                user.getConn().append(msg.encode("utf8"))
