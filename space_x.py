class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def load_wallet(self, amount):
        self.balance += amount

    def travel(self, source, destination, rocket):
        # initialize fare to zero
        fare = 0
        # check if source and destination are in the same orbit
        if source.orbit == source.orbit:
            # add 50 to the fare
            fare += 50
        # otherwise,
        else:
            # add 250 to the fare
            fare += 250
        # check if rocket is a luxury rocket
        if rocket.is_luxury:
            # double the fare
            fare *= 2
        # check if destination station_type is man_made
        if destination.station_type == "manmade":
            # add 200 to the fare
            fare += 200
        # deduct the fare from the balance
        self.balance -= fare

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
