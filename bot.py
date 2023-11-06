import socket
import time
import importlib as implib
from modules.procesos import *
from modules.defs import *
from modules.vars import *




while True:  # Mientras el bot esté funcionando
    try:
        ircsock = connect()
        while True:
            ircmsg = ircsock.recv(2048).decode("utf-8")
            ircmsg = ircmsg.strip('\n\r')
            print(ircmsg)
            if ircmsg.find("PRIVMSG") != -1:
                comandos(ircmsg)
            if ircmsg.find("PING :") != -1:  # Si el servidor nos envía un mensaje PING, le respondemos con un PONG
                ping_msg = ircmsg.split(':')[1]
                ping(ircsock, ping_msg)

            if ircmsg.find("372") != -1:  # Si el servidor nos envía un mensaje PING, le respondemos con un PONG
                ircsock.send(bytes(f"JOIN {channel} \r\n", "UTF-8"))  # Aquí se asigna el nick al bot

            if ircmsg.find(":@rehash") != -1:
                import modules.procesos as proc
                from modules.procesos import *
                
                implib.reload(proc)
                import modules.procesos as proc
                from modules.procesos import *
                
                ircsock.send(bytes(f"PRIVMSG #test Rehash \r\n", "UTF-8"))  # Aquí se asigna el nick al bot
    except (socket.error, socket.timeout):  # Si se produce un error (como una desconexión), volvemos a conectarnos
        print("Se ha producido un error. Reconectando en 15 segundos...")
        time.sleep(15)
        ircsock = connect()




