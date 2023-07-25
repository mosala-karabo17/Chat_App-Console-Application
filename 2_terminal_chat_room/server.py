# server side chat room

import socket
import threading

# Define constants to be used 
HOST_IP = socket.gethostbyname(socket.gethostname)
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

# create a server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST_PORT, HOST_PORT))
serverSocket.listen()

# create two blank list to store connect client socket and their names
client_socket_list = []
client_name_list = []


def broadcast_message(message):
    # send a message to all clients connected to the server

    pass

def receive_message(client_socket):
    # receive an incoming message from specific client and forward the message to be broadcast
    pass

def connect_client():
    # connect an incoming client to the server
    pass



