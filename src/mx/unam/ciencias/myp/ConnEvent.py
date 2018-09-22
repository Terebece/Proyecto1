from enum import Enum

class ConnEvent(Enum):
    """
    Enumeración para los eventos que puede genera una conexión entre el servidor
    y el cliente.
    """
    CREATEROOM = "CREATEROOM"
    DISCONNECT = "DISCONNECT"
    IDENTIFY = "IDENTIFY"
    HELP = "HELP"
    INVITE = "INVITE"
    JOINROOM = "JOINROOM"
    MESSAGE = "MESSAGE"
    PUBLICMESSAGE = "PUBLICMESSAGE"
    ROOMMESSAGE = "ROOMESSAGE"
    STATUS = "STATUS"
    USERS = "USERS"
