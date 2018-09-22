import random
import sys
import socket
import threading
import unittest
import Client
import Server

class TestServer(unittest.TestCase):

    def testGetAddress(self):
        """
        Prueba unitaria para getAddress.
        """
        self.server = Server.Server("localhost", 3456)
        self.server.setAddress("localhost", 3459)
        self.assertEqual(("localhost", 3459), self.server.getAddress())
        self.server.getSocket().close()

    def testSetAddress(self):
        """
        Prueba unitaria para setAddress.
        """
        self.server = Server.Server("localhost", 3456)
        self.server.setAddress(("localhost", 3457))
        self.assertEqual(("localhost", 3457), self.server.getAddress())
        self.server.getSocket().close()

    def testSetSocket(self):
        """
        Prueba unitaria para setSocket.
        """
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = Server.Server("localhost", 3456)
        self.server.setSocket(self.serverSocket)
        self.assertEqual(self.serverSocket, self.server.getSocket())
        self.serverSocket.close()
        self.server.getSocket().close()

    def testGetSocket(self):
        """
        Prueba unitaria para getSocket.
        """
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = Server.Server("localhost", 3456)
        self.server.setSocket(self.serverSocket)
        self.assertEqual(self.serverSocket, self.server.getSocket())
        self.serverSocket.close()
        self.server.getSocket().close()

    def testRunServer(self):
        """
        Prueba unitaria para runServer.
        """
        pass

    def testCreatSocket(self):
        """
        Prueba unitaria para creatSocket.
        """
        pass

    def testCreatThreading(self):
        """
        Prueba unitaria para creatThreading.
        """
        pass

    def testMsgAll(self):
        """
        Prueba unitaria para msgAll.
        """
        pass

    def testAcceptConn(self):
        """
        Prueba unitaria para acceptConn.
        """
        pass

    def testProcessConn(self):
        """
        Prueba unitaria para processConn.
        """
        pass

if __name__ == "__main__":
    unittest.main()
