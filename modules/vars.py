#variables
import socket
server = "irc.chathispano.com"  # Servidor de IRC
channel = "#test"  # Canal de IRC
botnick = "PrEtOrIaN"  # Nombre del bot
botpass = "pf5bDdRa72zB"

global ircsock
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)