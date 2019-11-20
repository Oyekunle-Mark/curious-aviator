class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def load_wallet(self, amount):
        self.balance += amount


class Station:
    def __init(self, name, station_type, orbit):
        self.name = name
        self.station_type = station_type
        self.orbit = orbit


class Rocket:
    def __init__(self, name, is_luxury):
        self.name = name
        self.is_luxury = is_luxury
