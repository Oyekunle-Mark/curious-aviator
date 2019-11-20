class User:
    """User class"""

    def __init__(self, name):
        self.name = name
        self.balance = 0

    def load_wallet(self, amount):
        """Adds BTC to the wallet"""
        self.balance += amount

    def travel(self, source, destination, rocket):
        """Calculates and deducts the fare from the wallet's balance"""
        fare = 0

        if source.orbit == destination.orbit:
            fare += 50
        else:
            fare += 250

        if rocket.is_luxury:
            fare *= 2

        if destination.station_type == "manmade":
            fare += 200

        self.balance -= fare

    @property
    def wallet_balance(self):
        return self.balance


class Station:
    """Station class"""

    def __init__(self, name, station_type, orbit):
        self.name = name
        self.station_type = station_type
        self.orbit = orbit


class Rocket:
    """Rocket class"""

    def __init__(self, name, is_luxury):
        self.name = name
        self.is_luxury = is_luxury
