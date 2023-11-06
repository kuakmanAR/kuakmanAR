#Definiciones
import socket, time
from modules.vars import *
def canal(cadena):
 canal = cadena.split('PRIVMSG', 1)[1].split(':', 1)[0].strip()
 return canal

def usuario(cadena):
    sender = cadena.split('!')[0][1:]
    return sender
def mensaje(cadena):
    message = cadena.split('PRIVMSG', 1)[1].split(':', 1)[1].strip()
    return message

def connect():
    
    ircsock.connect((server, 6667))  # Aquí se conecta al servidor
    ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick +" :Este es mi bot de IRC\n", "UTF-8"))
    ircsock.send(bytes("NICK "+ botnick +"!"+botpass+"\n", "UTF-8"))  # Aquí se asigna el nick al bot
    
    return ircsock

def ping(ircsock, msg):  # Esta función responde a los mensajes de ping del servidor
    ircsock.send(bytes("PONG :" + msg + "\n", "UTF-8"))
