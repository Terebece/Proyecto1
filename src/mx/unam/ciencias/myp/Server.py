import socket
import sys
import threading

class Server():

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, host, port):
        """
        Metodo que inicializa el servidor con la direccion que va a tener el
        servidor y una lista de los clientes que se van a ir conectando
        """
        self.host = host
        self.port = port
        self.addr = (self.host, self.port)
        self.clients = []

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
        print("Server Ready")
        self.creatThreading()
        while True:
            msg = input()
            if msg == '_salir':
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

    def creatThreading(self):
        """
        Metodo que se encarga de crear dos hilos de ejecucion para que el servidor
        pueda aceptar y procesar los mensajes de los clientes
        """

        accept = threading.Thread(target=self.acceptConn)
        process = threading.Thread(target=self.processConn)

        accept.daemon = True
        accept.start()

        process.daemon = True
        process.start()

    def msgAll(self, msg, client):
        """
        Metodo que envia mensaje a todos los clientes conectados al servidor
        """
        for conn in self.clients:
            try:
                if conn != client:
                    conn.send(msg)
            except:
                self.clients.remove(conn)

    def acceptConn(self):
        """
        Metodo que acepta las conexiones de los clientes
        """
        while True:
            try:
                conn, addr = self.serverSocket.accept()
                conn.setblocking(False)
                self.clients.append(conn)
                print('%s connected to the server'% addr[0])
                conn.send("Bienvenido al chat".encode("utf8"))
            except:
                pass

    def processConn(self):
        """
        Metodo que procesa las conexiones de los clientes
        """
        while True:
            if len(self.clients) > 0:
                for conn in self.clients:
                    try:
                        msg = conn.recv(1024)
                        if msg:
                            self.msgAll(msg, conn)
                    except:
                        pass
