import random
import sys
import socket
import threading
import unittest
import Client
import Server

class TestServer(unittest.TestCase):

    def testGetAddress(self):
        self.server = Server.Server("localhost", 3456)
        self.server.setAddress("localhost", 3459)
        self.assertEqual(("localhost", 3459), self.server.getAddress())
        self.server.getSocket().close()

    def testSetAddress(self):
        self.server = Server.Server("localhost", 3456)
        self.server.setAddress(("localhost", 3457))
        self.assertEqual(("localhost", 3457), self.server.getAddress())
        self.server.getSocket().close()

    def testSetSocket(self):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = Server.Server("localhost", 3456)
        self.server.setSocket(self.serverSocket)
        self.assertEqual(self.serverSocket, self.server.getSocket())
        self.serverSocket.close()
        self.server.getSocket().close()

    def testGetSocket(self):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = Server.Server("localhost", 3456)
        self.server.setSocket(self.serverSocket)
        self.assertEqual(self.serverSocket, self.server.getSocket())
        self.serverSocket.close()
        self.server.getSocket().close()

    def testRunServer(self):
        pass

    def testCreatSocket(self):
        pass

    def testCreatThreading(self):
        pass

    def testMsgAll(self):
        pass

    def testAcceptConn(self):
        pass

    def testProcessConn(self):
        pass

if __name__ == "__main__":
    unittest.main()
