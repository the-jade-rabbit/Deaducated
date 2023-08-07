"""second half of serverSS, Client side"""
import socket

##
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 2401))
print("recieved: {0}".format(client.recv(1024)))
client.close()