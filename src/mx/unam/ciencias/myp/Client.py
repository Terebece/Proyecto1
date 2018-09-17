import socket
import threading
import sys

class Client():
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.addr = (self.host, self.port)

    def setAddress(self, addr):
        self.addr = addr

    def getAddress(self):
        return self.addr

    def setSocket(self, socket):
        self.clientSock.close()
        self.clientSock = socket

    def getSocket(self):
        return self.clientSock

    def runClient(self):
        self.clientSock.connect(self.addr)
        self.creatThreading()
        while True:
            msg = sys.stdin.readline()
            if '_salir' in msg:
                self.clientSock.close()
                sys.exit()
            else:
                self.msgSend(msg)

    def creatThreading(self):
        msgRecv = threading.Thread(target=self.msgRecv)
        msgRecv.daemon = True
        msgRecv.start()

    def msgRecv(self):
        while True:
            try:
                msg = self.clientSock.recv(1024).decode("utf8")
                if msg:
                    print(msg)
            except:
                pass

    def msgSend(self, msg):
        self.clientSock.send(msg.encode("utf8"))
        self.clearLine()
        sys.stdout.write("<You>")
        sys.stdout.write(msg)
        sys.stdout.flush()

    def clearLine(self):
        CURSOR_UP = '\033[F'
        ERASE_LINE = '\033[K'
        print(CURSOR_UP + ERASE_LINE)
