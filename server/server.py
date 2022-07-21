from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time

from server.account import account


HOST = 'localhost'
PORT = 5500
BUFSIZE = 512
ADDR = (HOST , PORT)


def broadcast():



def handle_client(account):
    name = account.name
    ADDR = account.ADDR
    while True:
        msg = account.recv(BUFSIZE)
        if msg == bytes("{Quit}", "utf8"):
            account.close()
        else:




def wait_for_connection():
    run = True
    while run:
        try:
            client, ADDR = SERVER.accept()
            account = account(ADDR, name, client)
            print(f"[CONNECTION] {ADDR} connected to the server at {time.time()}")
            Thread(target=handle_client, args=(account)).start()
        except Exception as e:
            print("[FAILURE]", e)
            run = False

    print("SERVER CRASHED")


SERVER = socket(AF_INET , SOCK_STREAM)
SERVER.bind(ADDR)


if __name__ == '__main__':
    SERVER.listen(5)
    print("waiting for connection")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
