import socket
import threading
import sys

class Client():

    def __init__(self, host, port):
        """
        Metodo que inicializa un cliente con la direccion para el socket
        """
        self.addr = (host, port)
        self.clientRunning = True
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def setAddress(self, addr):
        """
        Metodo que define la direccion con la cual se va conectar al servidor
        """
        self.addr = addr

    def getAddress(self):
        """
        Metodo que regresa la direccion con la cual se va conectar al servidor
        """
        return self.addr

    def setSocket(self, socket):
        """
        Metodo que define un nuevo socket para el cliente
        """
        self.clientSock.close()
        self.clientSock = socket

    def getSocket(self):
        """
        Metodo que regresa el socket
        """
        return self.clientSock

    def runClient(self):
        """
        Metodo que se encarga de conectar al cliente con el servidor
        """
        self.clientSocket.connect(self.addr)
        self.creatThreading()
        while self.clientRunning:
            msg = input()
            if 'DISCONNECT' in msg:
                self.clientRunning = False
                self.clientSocket.send("DISCONNECT".encode("utf8"))
            else:
                self.msgSend(msg)

    def creatThreading(self):
        """
        Metodo que se encarga de crear un hilo de ejecucion para que el cliente
        pueda recivir mensajes del Servidor
        """
        msgRecv = threading.Thread(target=self.msgRecv)
        msgRecv.daemon = True
        msgRecv.start()

    def msgRecv(self):
        """
        Metodo que se encarga de recivir los mensajes del servidor
        """
        while self.clientRunning:
            try:
                msg = self.clientSocket.recv(1024).decode("utf8")
                if msg:
                    print(msg)
            except:
                print("El servidor se cayo.")
                self.clientRunning = False

    def msgSend(self, msg):
        """
        Metodo que se encarga de enviar mensajes al servidor y cliente
        """
        self.clientSocket.send(msg.encode("utf8"))
        self.clearLine()
        sys.stdout.write("<You> ")
        sys.stdout.write(msg + "\n")
        sys.stdout.flush()

    def clearLine(self):
        """
        Metodo que borra la linea que se mete en la terminal
        """
        CURSOR_UP = '\033[F'
        ERASE_LINE = '\033[K'
        print(CURSOR_UP + ERASE_LINE)

if __name__ == '__main__':
    host = str(input("Enter host: "))
    port = int(input("Enter port: "))

    client = Client(host, port)
    client.runClient()
