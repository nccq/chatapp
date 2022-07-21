from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time
from unicodedata import name

from account import account


HOST = 'localhost'
PORT = 5500
BUFSIZE = 512
ADDR = (HOST , PORT)
accounts = []
SERVER = socket(AF_INET , SOCK_STREAM)
SERVER.bind(ADDR)


def broadcast(msg, name):
    for account in accounts:
        client = account.client
        client.send(bytes(name + ":", "utf8") + msg)



def handle_client(account):
    client = account.client
    name = client.recv(BUFSIZE).decode("urf8")
    msg = f"{name} has joind the chat"
    broadcast(msg)


    while True:
        try:
            msg = client.recv(BUFSIZE)
            print(f"{name}:", msg.decode("utf8"))
            if msg == bytes("{Quit}", "utf8"):
                broadcast(f"{name} has left the chat", "")
                client.send(bytes("{Quit}", "utf8"))
                client.close()
                accounts.remove(account)
                break
            else:
                broadcast(msg, name)
        except Exception as e:
             print("[EXCEPTION]", e)
             break




def wait_for_connection():
    run = True
    while run:
        try:
            client, ADDR = SERVER.accept()
            account = account(ADDR, name, client)
            accounts.append(account)
            print(f"[CONNECTION] {ADDR} connected to the server at {time.time()}")
            Thread(target=handle_client, args=(account)).start()
        except Exception as e:
            print("[EXCEPTION]", e)
            run = False

    print("SERVER CRASHED")


if __name__ == '__main__':
    SERVER.listen(5)
    print("waiting for connection")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
