import socket
import threading
import sys

class Client():

    def __init__(self, host, port):
        """
        Constructor que inicializa un cliente con la dirección que utilizara para
        conectarse con el servidor.
        """
        self.addr = (host, port)
        self.clientRunning = True
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def setAddress(self, addr):
        """
        Función que define la dirección con la cual se va conectar al servidor.
        """
        self.addr = addr

    def getAddress(self):
        """
        Función que regresa la dirección con la cual se va conectar al servidor.
        """
        return self.addr

    def setSocket(self, socket):
        """
        Función que define un nuevo socket para el cliente.
        """
        self.clientSock.close()
        self.clientSock = socket

    def getSocket(self):
        """
        Función que regresa el socket.
        """
        return self.clientSock

    def runClient(self):
        """
        Función que se encarga de conectar al cliente con el servidor.
        """
        self.clientSocket.connect(self.addr)
        self.creatThreading()
        while self.clientRunning:
            msg = input()
            if 'DISCONNECT' in msg:
                self.clientRunning = False
                self.clientSocket.send("DISCONNECT".encode("utf8"))
            else:
                self.clientSocket.send(msg.encode("utf8"))

    def creatThreading(self):
        """
        Función que se encarga de crear un hilo de ejecución para que el cliente
        pueda recivir mensajes del Servidor.
        """
        msgRecv = threading.Thread(target=self.msgRecv)
        msgRecv.daemon = True
        msgRecv.start()

    def msgRecv(self):
        """
        Función que se encarga de recivir los mensajes del servidor.
        """
        while self.clientRunning:
            try:
                msg = self.clientSocket.recv(1024).decode("utf8")
                if msg:
                    print(msg)
            except:
                print("El servidor se cayo.")
                self.clientRunning = False

if __name__ == '__main__':
    host = str(input("Enter host: "))
    port = int(input("Enter port: "))

    client = Client(host, port)
    client.runClient()
