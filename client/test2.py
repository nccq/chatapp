from client import client



c1 = client("Tom")
c2 = client("Jake")

c1.send_message("Hi")
c2.send.message("Hello")

c1.disconnect()
c2.disconnect()