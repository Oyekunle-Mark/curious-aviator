class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def load_wallet(self, amount):
        self.balance += amount

    def travel(self, source, destination, rocket):
        # initialize fare to zero
        # check if source and destination are in the same orbit
            # add 50 to the fare
        # otherwise,
            # add 250 to the fare
        # check if rocket is a luxury rocket
            # double the fare
        # check if destination station_type is man_made
            # add 200 to the fare
        # deduct the fare from the balance
        pass

    @property
    def balance(self):
        return self.balance


class Station:
    def __init(self, name, station_type, orbit):
        self.name = name
        self.station_type = station_type
        self.orbit = orbit


class Rocket:
    def __init__(self, name, is_luxury):
        self.name = name
        self.is_luxury = is_luxury
