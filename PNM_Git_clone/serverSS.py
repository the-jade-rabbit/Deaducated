"""sample code ot simulate server to client comms"""
import socket

##
def respond(client):
    """generate client to server request pg"""
    response = input("enter a vlaue: ")
    client.send(bytes(response, "utf8"))
    client.close()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 2401))
    server.listen(1)

    try:
        while True:
            client, addr = server.accept()
            respond(client)
    finally:
        server.close()
