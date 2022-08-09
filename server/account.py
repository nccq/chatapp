class Account:
    def __init__(self, ADDR, client):
        self.ADDR = ADDR
        self.client = client
        self.name = None

    def set_name(self, name):
        self.name = name


    def __repr__(self):
        return f"Account({self.ADDR}, {self.name})"