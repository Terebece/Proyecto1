import socket
import sys
import threading

class Server():

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.addr = (self.host, self.port)
        self.clients = []

    def getAddress(self):
        return self.addr

    def setAddress(self, addr):
        self.addr = addr

    def setSocket(self, socket):
        self.serverSocket.close()
        self.serverSocket = socket

    def getSocket(self):
        return self.serverSocket

    def runServer(self):
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
        self.serverSocket.bind(self.addr)
        self.serverSocket.listen(100)
        self.serverSocket.setblocking(False)

    def creatThreading(self):
        accept = threading.Thread(target=self.acceptConn)
        process = threading.Thread(target=self.processConn)

        accept.daemon = True
        accept.start()

        process.daemon = True
        process.start()

    def msgAll(self, msg, client):
        for conn in self.clients:
            try:
                if conn != client:
                    conn.send(msg)
            except:
                self.clients.remove(conn)

    def acceptConn(self):
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
        while True:
            if len(self.clients) > 0:
                for conn in self.clients:
                    try:
                        msg = conn.recv(1024)
                        if msg:
                            self.msgAll(msg, conn)
                    except:
                        pass
