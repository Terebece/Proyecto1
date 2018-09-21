import unittest
import User

class TestUser(unittest.TestCase):

    def testSetConn(self):
        self.user = User.User("prueba", "0.0.0.0")
        self.assertEqual("prueba", self.user.getConn())
        self.user.setConn("PruebaCambio")
        self.assertEqual("PruebaCambio", self.user.getConn())

    def testGetConn(self):
        self.user = User.User("prueba1", "0.0.0.0")
        self.assertEqual("prueba1", self.user.getConn())
        self.user.setConn("PruebaCambio1")
        self.assertEqual("PruebaCambio1", self.user.getConn())

    def testSetAddress(self):
        self.user = User.User("prueba2", "0.0.0.0")
        self.assertEqual("0.0.0.0", self.user.getAddress())
        self.user.setAddress("0.1.0.0")
        self.assertEqual("0.1.0.0", self.user.getAddress())

    def testGetAddress(self):
        self.user = User.User("prueba3", "0.0.0.0")
        self.assertEqual("0.0.0.0", self.user.getAddress())
        self.user.setAddress("0.1.0.0")
        self.assertEqual("0.1.0.0", self.user.getAddress())

    def testGetName(self):
         self.user = User.User("prueba4", "0.0.0.0")
         self.assertEqual(" ", self.user.getName())
         self.user.setName("Teresa")
         self.assertEqual("Teresa", self.user.getName())

    def testSetName(self):
        self.user = User.User("prueba5", "0.0.0.0")
        self.assertEqual(" ", self.user.getName())
        self.user.setName("Teresa")
        self.assertEqual("Teresa", self.user.getName())

    def testGetIdentified(self):
        self.user = User.User("prueba6", "0.0.0.0")
        self.user.setName("Teresa")
        self.assertEqual(True, self.user.getIdentified())

    def testGetStatus(self):
        self.user = User.User("prueba7", "0.0.0.0")
        self.assertEqual("ACTIVE", self.user.getStatus())
        self.user.setStatus("BUSY")
        self.assertEqual("BUSY", self.user.getStatus())

    def testSetStatus(self):
        self.user = User.User("prueba8", "0.0.0.0")
        self.assertEqual("ACTIVE", self.user.getStatus())
        self.user.setStatus("AWAY")
        self.assertEqual("AWAY", self.user.getStatus())


if __name__ == "__main__":
    unittest.main(argv = ["ignored", "-v"], exit = False)
