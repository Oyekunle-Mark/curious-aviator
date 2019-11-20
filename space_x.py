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


if __name__ == "__main__":
    # instantiate the user
    user = User("Lone Voyager")

    # instantiate the stations
    abuja = Station("Abuja", "natural", "earth")
    spock = Station("Spock", "natural", "mars")
    iss = Station("ISS", "manmade", "earth")
    moon = Station("Abuja", "natural", "earth")

    # instantiate the rockets
    falcon_1 = Rocket("Falcon 1", False)
    falcon_9 = Rocket("Falcon 9", True)

    # load the wallet with 3000BTC
    user.load_wallet(3000)
    # take trips
    user.travel(abuja, moon, falcon_9)
    user.travel(moon, spock, falcon_1)
    user.travel(spock, iss, falcon_9)

    print(
        f"After the trips, {user.name}'s balance is {user.wallet_balance}BTC")
