import unittest
import threading
import socket
import sys
import Client
import Server

class TestCliente(unittest.TestCase):

    def testSetAddress(self):
        """
        Pruebas unitarias para setAddress.
        """
        self.client = Client.Client("localhost", 3456)
        self.client.setAddress(("localhost",3457))
        self.assertEqual(("localhost",3457), self.client.getAddress())
        self.client.getSocket().close()

    def testGetAddress(self):
        """
        Pruebas unitarias para getAddress.
        """
        self.client = Client.Client("localhost", 3456)
        self.client.setAddress(("localhost",3457))
        self.assertEqual(("localhost",3457), self.client.getAddress())
        self.client.getSocket().close()

    def testSetSocket(self):
        """
        Pruebas unitarias para setSocket.
        """
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = Client.Client("localhost", 3456)
        self.client.setSocket(self.clientSocket)
        self.assertEqual(self.clientSocket, self.client.getSocket())
        self.clientSocket.close()
        self.client.getSocket().close()

    def testGetSocket(self):
        """
        Pruebas unitarias para getSocket.
        """
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = Client.Client("localhost", 3456)
        self.client.setSocket(self.clientSocket)
        self.assertEqual(self.clientSocket, self.client.getSocket())
        self.clientSocket.close()
        self.client.getSocket().close()

    def testRunClient(self):
        """
        Pruebas unitarias para runClient.
        """
        pass

    def testCreatThreading(self):
        """
        Pruebas unitarias para creatThreading.
        """
        pass

    def testMsgRecv(self):
        """
        Pruebas unitarias para msgRecv.
        """
        pass

    def testSendMsg(self):
        """
        Pruebas unitarias para sendMsg.
        """
        pass

if __name__ == "__main__":
    unittest.main()
