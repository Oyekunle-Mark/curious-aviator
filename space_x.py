class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def load_wallet(self, amount):
        self.balance += amount
