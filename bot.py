import socket
import time

server = "irc.chathispano.com"  # Servidor de IRC
channel = "#test"  # Canal de IRC
botnick = "PrEtOrIaN"  # Nombre del bot
botpass = "pf5bDdRa72zB"
def ping(ircsock, msg):  # Esta función responde a los mensajes de ping del servidor
    ircsock.send(bytes("PONG :" + msg + "\n", "UTF-8"))

def connect():
    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ircsock.connect((server, 6667))  # Aquí se conecta al servidor
    ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick +" :Este es mi bot de IRC\n", "UTF-8"))
    ircsock.send(bytes("NICK "+ botnick +"!"+botpass+"\n", "UTF-8"))  # Aquí se asigna el nick al bot

    return ircsock

while True:  # Mientras el bot esté funcionando
    try:
        ircsock = connect()
        while True:
            ircmsg = ircsock.recv(2048).decode("UTF-8")
            ircmsg = ircmsg.strip('\n\r')
            print(ircmsg)

            if ircmsg.find("PING :") != -1:  # Si el servidor nos envía un mensaje PING, le respondemos con un PONG
                ping_msg = ircmsg.split(':')[1]
                ping(ircsock, ping_msg)

            if ircmsg.find("372") != -1:  # Si el servidor nos envía un mensaje PING, le respondemos con un PONG
                ircsock.send(bytes(f"JOIN {channel} \r\n", "UTF-8"))  # Aquí se asigna el nick al bot

    except (socket.error, socket.timeout):  # Si se produce un error (como una desconexión), volvemos a conectarnos
        print("Se ha producido un error. Reconectando en 15 segundos...")
        time.sleep(15)
        ircsock = connect()




