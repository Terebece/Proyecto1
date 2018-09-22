import unittest
import Room

class TestRoom(unittest.TestCase):

    def testSetRoomName(self):
        """
        Prueba unitaria para setRoomName.
        """
        self.room = Room.Room("Nueva", "Teresa")
        self.assertEqual("Nueva", self.room.getRoomName())
        self.room.setRoomName("Prueba")
        self.assertEqual("Prueba", self.room.getRoomName())

    def testGetRoomName(self):
        """
        Prueba unitaria para getRoomName.
        """
        self.room1 = Room.Room("Nueva1", "Carmen")
        self.assertEqual("Nueva1", self.room1.getRoomName())
        self.room1.setRoomName("Prueba1")
        self.assertEqual("Prueba1", self.room1.getRoomName())

    def testAddGuestUsers(self):
        """
        Prueba unitaria para addGuestUsers.
        """
        self.room3 = Room.Room("Nueva", "Juan")
        self.assertEqual([], self.room3.getGuestUser())
        self.lista = ["Teresa", "Carmen", "Julia"]
        self.room3.addGuestUsers("Juan", self.lista)
        self.assertEqual(["Teresa", "Carmen", "Julia"], self.room3.getGuestUser())

    def testAddUsersInRoom(self):
        """
        Prueba unitaria para addUsersInRoom.
        """
        self.room4 = Room.Room("Nueva", "Luci")
        self.assertEqual([], self.room4.getUsersInRoom())
        self.room4.addUsersInRoom("Enrique")
        self.assertEqual(["Enrique"], self.room4.getUsersInRoom())

    def testGetGuestUser(self):
        """
        Prueba unitaria para getGuestUser.
        """
        self.room5 = Room.Room("Nueva", "Enrique")
        self.assertEqual([], self.room5.getGuestUser())
        self.lista = ["Teresa", "Carmen", "Julia"]
        self.room5.addGuestUsers("Enrique", self.lista)
        self.assertEqual(["Teresa", "Carmen", "Julia"], self.room5.getGuestUser())

    def testGetUsersInRoom(self):
        """
        Prueba unitaria para getUsersInRoom.
        """
        self.room6 = Room.Room("Nueva", "Marco")
        self.assertEqual([], self.room6.getUsersInRoom())
        self.room6.addUsersInRoom("Daniel")
        self.assertEqual(["Daniel"], self.room6.getUsersInRoom())


if __name__ == "__main__":
    unittest.main(argv = ["ignored", "-v"], exit = False)
