from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time


HOST = 'localhost'
PORT = 5500
BUFSIZE = 512
ADDR = (HOST , PORT)


messages = []
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)


def recive_messages():
    while True:
        try:
            msg = client_socket.recv(BUFSIZE).decode()
            messages.append(msg)
            print(msg)
        except Exception as e:
            print("EXCEPTION", e)
            break


def send_message(msg):
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()


recive_thread = Thread(target=recive_messages)
recive_thread.start()


send_message("Lukas")
time.sleep(10)
send_message("Hello world")
