import time
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

from account import Account

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
        try:
            client.send(bytes(name, "utf8") + msg)
        except Exception as e:
            print("[EXCEPTION]", e)



def handle_client(account):
    client = account.client
    name = client.recv(BUFSIZE).decode("utf8")
    account.set_name(name)   
    msg = bytes(f"{name} has joind the chat", "utf8")
    broadcast(msg, "")


    while True:
        
            msg = client.recv(BUFSIZE)
            if msg == bytes("{Quit}", "utf8"):
                client.close()
                accounts.remove(account)
                broadcast(bytes(f"{name} has left the chat", "utf8"), "")
                print(f"[DISCONNECTED] {name} disconnected")
                break
            else:
                broadcast(msg, name+" :")
                print(f"{name}:", msg.decode("utf8"))





def wait_for_connection():
    while True:
        try:
            client, ADDR = SERVER.accept()
            account = Account(ADDR, client)
            accounts.append(account)
            print(f"[CONNECTION] {ADDR} connected to the server at {time.time()}")
            Thread(target=handle_client, args=(account,)).start()
        except Exception as e:
            print("[EXCEPTION]", e)
            break

    print("SERVER CRASHED")


if __name__ == "__main__":
    SERVER.listen(10)
    print("waiting for connection")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
