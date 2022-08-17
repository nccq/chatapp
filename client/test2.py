from client import client
import time
from threading import Thread


c1 = client("Tom")
c2 = client("Jake")


def update_messages():
    msgs = []
    run = True
    while run:
        time.sleep(0.1)
        new_messages = c1.get_messages()
        msgs.extend(new_messages)
        for msg in new_messages:
            print(msg)
            if msg == "{quit}":
                run = False
                break


Thread(target=update_messages).start()


c1.send_message("Hi")
time.sleep(5)
c2.send_message("Hello")
time.sleep(5)

c1.disconnect()
time.sleep(5)
c2.disconnect()

