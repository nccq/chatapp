from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread, Lock
import time


class client:

    HOST = 'localhost'
    PORT = 5500
    BUFSIZE = 512
    ADDR = (HOST , PORT)

    def __init__(self, name):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.ADDR)
        self.messages = []
        recive_thread = Thread(target=self.recive_messages)
        recive_thread.start()
        self.send_message(name)
        self.lock = Lock()


    def recive_messages(self):
        while True:
            try:
                msg = self.client_socket.recv(self.BUFSIZE).decode()
                self.lock.acquire()
                self.messages.append(msg)
                self.lock.release()
            except Exception as e:
                print("EXCEPTION", e)
                break


    def send_message(self, msg):
        self.client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            self.client_socket.close()


    def get_messages(self):
        msgs_copy = self.messages[:]
        self.lock.acquire()
        self.messages = []
        self.lock.release()
        return msgs_copy


    def disconnect(self):
        self.send_message("{quit}")