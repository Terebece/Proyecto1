import unittest
import threading
import socket
import sys
from myp import Client
from myp import Server

class TestCliente(unittest.TestCase):

    def testSetAddress(self):
        self.client = Client.Client("localhost", 3456)
        self.client.setAddress(("localhost",3457))
        self.assertEqual(("localhost",3457), self.client.getAddress())
        self.client.getSocket().close()

    def testGetAddress(self):
        self.client = Client.Client("localhost", 3456)
        self.client.setAddress(("localhost",3457))
        self.assertEqual(("localhost",3457), self.client.getAddress())
        self.client.getSocket().close()

    def testSetSocket(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = Client.Client("localhost", 3456)
        self.client.setSocket(self.clientSocket)
        self.assertEqual(self.clientSocket, self.client.getSocket())
        self.clientSocket.close()
        self.client.getSocket().close()

    def testGetSocket(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = Client.Client("localhost", 3456)
        self.client.setSock(self.clientSocket)
        self.assertEqual(self.clientSocket, self.client.getSocket())
        self.clientSocket.close()
        self.client.getSocket().close()

    def testRunClient():
        pass

    def testCreatThreading(self):
        pass

    def testMsgRecv(self):
        pass

    def testSendMsg(self):
        pass

if __name__ == "__main__":
    unittest.main()
