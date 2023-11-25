#procesos

from modules.vars import *
from modules.defs import *

def comandos(buffer):
    canal2 = canal(buffer)
    if buffer.find(":@123") != -1:  # Si el servidor nos envía un mensaje PING, le respondemos con un PONG
        ircsock.send(bytes(f"PRIVMSG {canal2} Hola1 \r\n", "UTF-8"))  # Aquí se asigna el nick al bot
