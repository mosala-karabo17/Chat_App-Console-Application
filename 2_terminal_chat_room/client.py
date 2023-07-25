# client side chat room

import socket
import threading

# Define constants to be used
DESTINATION_IP = socket.gethostbyname(socket.gethostname)
DESTINATION_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

# create a client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((DESTINATION_IP, DESTINATION_PORT))

def send_message():
    # send a message to the server to be broadcast

    pass

def receive_message(client_socket):
    # receive an incoming message from specific server
    pass