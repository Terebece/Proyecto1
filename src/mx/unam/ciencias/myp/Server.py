import socket
import sys
import threading
import User
import Room
import ConnEvent

class Server():

    userstatus = ["ACTIVE", "AWAY", "BUSY"]

    def __init__(self, host, port):
        """
        Función que inicializa el servidor con la dirección que va a tener el
        servidor, una lista de los clientes que se van a ir conectando, una
        lista de las salas del servidor
        """
        self.addr = (host, port)
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.rooms = []
        self.clientConnected = True
        self.verify = False


    def getAddress(self):
        """
        Función que regresa la dirección del servidor
        """
        return self.addr

    def setAddress(self, addr):
        """
        Función que define una nueva dirección al servidor
        """
        self.addr = addr

    def setSocket(self, socket):
        """
        Función que define un nuevo socket para el servidor
        """
        self.serverSocket.close()
        self.serverSocket = socket

    def getSocket(self):
        """
        Función que regresa el socket del servidor
        """
        return self.serverSocket

    def runServer(self):
        """
        Función que crea el servidor y lo deja en ejecución para que los clientes
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
        Función que crea un socket para el servidor
        """
        self.serverSocket.bind(self.addr)
        self.serverSocket.listen(100)
        self.serverSocket.setblocking(False)
        print("Servidor listo.")
        p = self.serverSocket.getsockname()
        print("El servidor se conecto en el puerto: %s" % p[1])


    def creatThreading(self):
        """
        Función que se encarga de crear dos hilos de ejecución para que el servidor
        pueda aceptar y procesar los mensajes de los clientes
        """
        accept = threading.Thread(target = self.acceptConn)
        process = threading.Thread(target=self.processConn)

        accept.daemon = True
        accept.start()

        process.daemon = True
        process.start()

    def acceptConn(self):
        """
        Función que acepta las conexiones de los clientes.
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

    def processConn(self):
        """
        Función que procesa las conexiones de los clientes
        """
        while True:
            if len(self.clients) > 0:
                for client in self.clients:
                    try:
                        msg = client.getConn().recv(1024).decode("utf8")
                        if msg:
                            aux = msg.split(" ")
                            if  msg.find("CREATEROOM", 0, 10) != -1:
                                self.creatRoom(aux[1], client)
                            elif msg == "DISCONNECT":
                                sefl.disconnect(client)
                            elif msg == "HELP":
                                self.help(client)
                            elif msg.find("IDENTIFY", 0, 8) != -1:
                                self.identify(msg, client)
                            elif msg.find("INVITE", 0, 6) != -1:
                                self.invite(msg, client)
                            elif msg.find("JOINROOM", 0, 8) != -1:
                                self.joinr(aux[1], client)
                            elif msg.find("MESSAGE", 0, 7) != -1:
                                self.message(aux[1], msg, client)
                            elif msg.find("PUBLICMESSAGE", 0, 13) != -1:
                                self.publicMsg(msg, client)
                            elif msg.find("ROOMESSAGE", 0, 10) != -1:
                                self.rooMsg(aux[1], msg, client)
                            elif msg.find("STATUS", 0, 6) != -1:
                                self.status(msg, client)
                            elif msg.find("USERS", 0, 5) != -1:
                                self.users(client)
                            else:
                                inva = "Mensaje invalido, escribe HELP para saber los comandos del chat"
                                client.getConn().send(inva.encode("utf8"))
                    except:
                        pass

    def creatRoom(self, roomname, client):
        """
        Función que crea una sala.
        """
        if client.getIdentified() != False:
            room = Room.Room(roomname, client.getName())
            self.rooms.append(room)
            ms = "Has creado la sala %s" % roomname
            client.getConn().send(ms.encode("utf8"))
        else:
            inv = "Identificate primero para poder crear una sala"
            client.getConn().send(inv.encode("utf8"))

    def disconnect(self, client):
        """
        Función auxiliar que desconecta a un cliente.
        """
        response = "Saliendo del servidor"
        client.getConn().send(response.encode("utf8"))
        print("%s se desconecto" % client.getName())

    def help(self, client):
        """
        Función auxiliar que nos regresa los comandos del chat.
        """
        h = "...CREATEROOM roomname\n" + "...DISCONNECT\n" + "...HELP\n"
        h += "...IDENTIFY username\n" +"...INVITE roomname username1 username2,...\n"
        h += "...JOINROOM roomname\n" + "...MESSAGE username messageContent\n"
        h += "...PUBLICMESSAGE messageContent\n" + "...ROOMESSAGE roomname "
        h += "messageContent\n" + "...STATUS userstatus\n" + "...USERS"
        client.getConn().send(h.encode("utf8"))

    def identify(self, msg, client):
        """
        Función auxiliar que identifica a los cliente.
        """
        name = msg.replace("IDENTIFY ", "")
        for c in self.clients:
            if c.getName() == name:
                self.verify = True
        if self.verify == False:
            client.setName(name)
            ms = "Te has identificado como %s" % name
            client.getConn().send(ms.encode("utf8"))
            self.connected(name)
        else:
            h = "Ese nombre no esta disponible, por favor introduce otro"
            client.getConn().send(h.encode("utf8"))

    def invite(self, guestU, client):
        """
        Función auxiliar que invita clientes a una sala.
        """
        if client.getIdentified() != False:
            guestU = guestU.replace("INVITE ", "")
            listUsers = guestU.split()
            roomname = listUsers.pop(0)
            for room in self.rooms:
                if room.getRoomName() == roomname:
                    room.addGuestUsers(client, listUsers)
                    h = "%s te invito a la sala %s" % (client.getName(), roomname)
                    for c in room.getGuestUser():
                        c.getConn().send(h.encode("utf8"))
        else:
            inv = "Identificate para poder invitar personas a una sala"
            client.getConn().send(inv.encode("utf8"))

    def joinr(self, roomname, client):
        """
        Función auxiliar que acepta una invitación a una sala.
        """
        if client.getIdentified() != False:
            for room in self.rooms:
                if room.getName() == roomname:
                    if client in room.getGuestUser():
                        room.addUsersInRoom(client)
                        ms = "Te has unido a la sala %s" % roomname
                        client.getConn().send(ms.encode("utf8"))
        else:
            inv = "Identificate para poder aceptar las invitaciones a salas"
            client.getConn().send(inv.encode("utf8"))

    def message(self, username, msg, client):
        """
        Función auxiliar que envia mensajes privados.
        """
        if client.getIdentified() != False:
            found = False
            for c in self.clients:
                if username == c.getName():
                    if client != c:
                        aux = "MESSAGE %s" % username
                        msg = msg.replace(aux, "")
                        auxMsg = "<" + client.getName() + ">" + msg
                        c.getConn().send(auxMsg.encode("utf8"))
                        found = True
                    if(not found):
                        client.send('Usuario invalido.'.encode("utf8"))
        else:
            inv = "Identificate para poder enviar mensajes privados"
            client.getConn().send(inv.encode("utf8"))

    def publicMsg(self, msg, client):
        """
        Función auxiliar que envía un mensaje publico.
        """
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
            client.getConn().send(inv.encode("utf8"))

    def rooMsg(self, roomname, msg, client):
        """
        Función auxiliar que envía un mensaje a la sala.
        """
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
            client.getConn().send(inv.encode("utf8"))

    def status(self, status, client):
        """
        Función auxiliar que cambia el estado de un cliente.
        """
        if client.getIdentified() != False:
            if msg.find("ACTIVE", 8, 13) != -1:
                client.setStatus("ACTIVE")
                client.getConn().send("Tu estado es: ACTIVE".encode("utf8"))
            elif status.find("AWAY", 8, 11) != -1:
                client.setStatus("AWAY")
                client.getConn().send("Tu estado es: AWAY".encode("utf8"))
            elif msg.find("BUSY", 8, 11) != -1:
                client.setStatus("BUSY")
                client.getConn().send("Tu estado es: BUSY".encode("utf8"))
            else:
                client.getConn().send("Estado invalido, por favor introduce alguno de los estados validos: ACTIVE, AWAY, BUSY")
        else:
            inv = "Identificate primero para poder cambiar de estado"
            client.getConn().send(inv.encode("utf8"))

    def users(self, client):
        """
        Función auxiliar que le envía la lista de clientes en el servidor a un cliente.
        """
        if client.getIdentified() != False:
            NoClient = 0
            response = "Lista de usuarios\n"
            for clien in self.clients:
                NoClient += 1
                response = response + str(NoClient) + ". " + clien.getName() + "\n"
            client.getConn().send(response.encode("utf8"))
        else:
            inv = "Identificate primero para poder ver la lista de usuarios"
            client.getConn().send(inv.encode("utf8"))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Correct usage: Server.py, port number")
        exit()

    host = "0.0.0.0"
    port = int(sys.argv[1])

    server = Server(host, port)
    server.runServer()
