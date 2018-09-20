import socket
import sys
import threading
import User
import Room
import PrivateRoom
import HandleClient

class Server():

    def __init__(self, host, port):
        """
        Metodo que inicializa el servidor con la direccion que va a tener el
        servidor y una lista de los clientes que se van a ir conectando
        """
        self.addr = (host, port)
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.rooms = []
        self.clientConnected = True

    def getAddress(self):
        """
        Metodo que regresa la direccion del servidor
        """
        return self.addr

    def setAddress(self, addr):
        """
        Metodo que define una nueva direccion al servidor
        """
        self.addr = addr

    def setSocket(self, socket):
        """
        Metodo que define un nuevo socket para el servidor
        """
        self.serverSocket.close()
        self.serverSocket = socket

    def getSocket(self):
        """
        Metodo que regresa el socket del servidor
        """
        return self.serverSocket

    def runServer(self):
        """
        Metodo que crea el servidor y lo deja en ejecucion para que los clientes
        se conecten a el
        """
        self.creatSocket()
        self.creatThreading()
        while True:
            msg = input()
            if msg == '___DISCONNECT___':
                self.serverSocket.close()
                sys.exit()
            else:
                pass

    def creatSocket(self):
        """
        Metodo que crea un socket para el servidor
        """
        self.serverSocket.bind(self.addr)
        self.serverSocket.listen(100)
        self.serverSocket.setblocking(False)
        print("Servidor listo.")
        p = self.serverSocket.getsockname()
        print("El servidor se conecto en el puerto: %s" % p[1])


    def creatThreading(self):
        """
        Metodo que se encarga de crear el hilo de ejecucion para que el servidor
        pueda aceptar y procesar los mensajes de los clientes
        """
        process = threading.Thread(target=self.processConn)
        process.daemon = True
        process.start()

    def msgAll(self, msg, client):
        """
        Metodo que envia mensaje a todos los clientes conectados al servidor
        """
        for client1 in self.clients:
            try:
                if client1 != client:
                    client1.getConn().send(msg)
            except:
                self.clients.remove(client1)

    def processConn(self):
        """
        Metodo que procesa las conexiones de los clientes
        """
        while True:
            try:
                conn, addr = self.serverSocket.accept()
                conn.setblocking(False)
                client = User.User(conn, addr[0])
                print('%s se ha conectado' % client.getAddress())
                client.getConn().send("Bienvenido al chat.\n".encode("utf8"))
                client.getConn().send("Identificate para poder utilizar el chat.\n".encode("utf8"))
                client.getConn().send("Escriba HELP para saber los comandos del chat\n".encode("utf8"))
                if conn not in self.clients:
                    self.clients.append(client)
            except socket.error:
                pass
            if len(self.clients) > 0:
                for client in self.clients:
                    try:
                        msg = client.getConn().recv(1024)
                        if msg:
                            self.msgAll(msg, client)
                    except:
                        pass

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Correct usage: Server.py, port number")
        exit()

    host = "0.0.0.0"
    port = int(sys.argv[1])

    server = Server(host, port)
    server.runServer()
