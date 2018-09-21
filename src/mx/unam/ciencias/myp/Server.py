import socket
import sys
import threading
import User
import Room
import EventoConexion

class Server():

    def __init__(self, host, port):
        """
        Metodo que inicializa el servidor con la direccion que va a tener el
        servidor y una lista de los clientes que se van a ir conectando
        """
        self.addr = (host, port)
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.clientsa = []
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
                    client1.getConn().send(msg.encode("utf8"))
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
                if conn not in self.clients:
                    self.clients.append(client)
            except socket.error:
                pass

            if len(self.clients) > 0:
                for client in self.clients:
                    try:
                        msg = client.getConn().recv(1024).decode("utf8")
                        if msg:
                            aux = msg.split(" ")
                            if "CREATEROOM" in msg:
                                self.creatRoom(aux[1], client)
                            elif "DISCONNECT" in msg:
                                sefl.disconnect(client)
                            elif "HELP" in msg:
                                self.help(client)
                            elif "IDENTIFY" in msg:
                                self.nameClient(client)
                            elif "INVITE" in msg:
                                self.invite(msg, client)
                            elif "JOINROOM" in msg:
                                self.joinr(aux[1], client)
                            elif "MESSAGE" in msg:
                                self.message(aux[1], msg, client)
                            elif  msg.find("PUBLICMESSAGE", 0, 13) != -1:
                                self.publicMsg(msg, client)
                            elif "ROOMESSAGE" in msg:
                                self.rooMsg(aux[1], msg, client)
                            elif "STATUS" in msg:
                                self.status(aux[1], client)
                            elif "USERS" in msg:
                                self.users(client)
                            else:
                                inva = "Mensaje invalido, escribe HELP para saber los comandos del chat"
                                client.getConn().send(inva.encode("utf8"))
                    except:
                        pass

    def creatRoom(self, roomname, client):
        if client.getIdentified() != False:
            room = Room.Room(roomname, client.getName())
            self.rooms.append(room)
        else:
            inv = "Identificate primero para poder crear una sala"
            client.getConn().send(inv.encode("utf8"))

    def disconnect(self, client):
        response = "Saliendo del servidor"
        client.getConn().send(response.encode("utf8"))
        print("%s se desconecto" % client.getName())
        client.setStatus("DISCONNECT")
        self.discont()

    def help(self, client):
        help = self.msgHelp()
        client.getConn().send(help.decode("utf8"))

    def invite(self, gustU, client):
        guestU = guestU.replace("INVITE ", "")
        listUsers = guestU.split()
        roomname = listUsers.pop(0)
        roomp = None
        for room in self.__rooms:
            if room.getRoomName() == roomname:
                room = roomp
        roomp.addGuestUsers(client, listUsers)
        h = "%s te invito a la sala %s" % (client.getName(), roomname)
        for c in roomp.getGuestUser():
            c.getConn().send(h.encode("utf8"))

    def nameClient(self, client):
        try:
            name = client.getConn().recv(1024).decode("utf8")
            if "IDENTIFY" in name:
                name = replace("IDENTIFY ", "")
                for c in self.clients:
                    if c.getName() == name:
                        self.verify = True
                    if self.verify == False:
                        client.setName(name)
                        self.clients.append(name)
                        self.connected(name)
                    else:
                        h = "Ese nombre no esta disponible, por favor introduce otro"
                        client.getConn().send(h.encode("utf8"))
                        self.nameClient()
                else:
                    pass
        except:
            pass

    def connected(self, name):
        for client in self.clients:
            try:
                client.getConn.send("Se conecto %s" % name).encode("utf8")
            except:
                pass

    def  discont(self, name):
        for client in self.clients:
            try:
                client.getConn.send("Se desconecto %s" % name).encode("utf8")
            except:
                pass

    def joinr(self, roomname, client):
        if client.getIdentified() != False:
            roomp = None
            for room in self.rooms:
                if room.getName() == roomname:
                    roomp = room
            if client in roomp.getGuestUser():
                roomp.addUsersInRoom(client)
        else:
            inv = "Identificate para poder aceptar las invitaciones a salas"

    def message(self, username, msg, client):
        if client.getIdentified() != False:
            found = False
            for c in self.__clients:
                if username == c.getName():
                    if client != c:
                        msg = msg.replace("MESSAGE" + username, "")
                        auxMsg = "<" + client.getName() + ">" + msg
                        c.getConn().send(auxMsg.encode('utf8'))
                        found = True
                    if(not found):
                        client.send('Usuario invalido.'.encode('utf8'))
        else:
            inv = "Identificate para poder enviar mensajes privados"
            client.getConn().send(inv.encode("utf8"))

    def publicMsg(self, msg, client):
        if client.getIdentified() != False:
            msg = msg.replace("PUBLICMESSAGE", "")
            auxMsg = "<" + client.getName() + ">" + msg
            for c in self.clients:
                try:
                    if c != client:
                        c.getConn().send(auxMsg.encode("utf8"))
                    else:
                        aux = "<You>" + msg
                        c.getConn().send(aux.encode("utf8"))
                except:
                    self.clients.remove(conn)
        else:
            inv = "Identificate para poder enviar mensajes publicos"

    def rooMsg(self, roomname, msg, client):
        if client.getIdentified() != False:
            msg = msg.replace("ROOMESSAGE" + roomname, "")
            auxMsg = "<" + client.getName() + ">" + msg
            room = None
            for roomt in self.rooms:
                if roomt.getRoomName() == roomname:
                    room = roomt
            room.msgInRoom(client, msg)
        else:
            inv = "Identificate primero para poder mensejes a una sala"

    def status(self, status, client):
        if client.getIdentified() != False:
            client.setStatus(status)
        else:
            inv = "Identificate primero para poder cambiar de estado"
            client.getConn().send(inv.encode("utf8"))

    def user(self, client):
        if client.getIdentified() != False:
            NoClient = 0
            response = "Lista de usuarios\n"
            for client in self.clients:
                NoClient += 1
                response = response + str(NoClient) + ". " + client.getName() + "\n"
            client.getConn().send(response.encode("utf8"))
        else:
            inv = "Identificate primero para poder ver la lista de usuarios"
            client.getConn().send(inv.encode("utf8"))

def msgHelp(self):
        h = "...CREATEROOM roomname\n" + "...DISCONNECT\n" + "...HELP\n"
        h += "...INVITE roomname username1 username2,...\n"
        h += "...JOINROOM roomname\n" + "...MESSAGE username messageContent\n"
        h += "...PUBLICMESSAGE messageContent\n" + "...ROOMESSAGE roomname"
        h += "messageContent\n" + "...STATUS userstatus" + "...USERS"
        return h

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Correct usage: Server.py, port number")
        exit()

    host = "0.0.0.0"
    port = int(sys.argv[1])

    server = Server(host, port)
    server.runServer()
