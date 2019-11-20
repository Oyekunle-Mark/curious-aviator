import unittest
from space_x import User, Station, Rocket


class TestSpaceX(unittest.TestCase):
    def test_new_user_balance(self):
        user = User("Lone Voyager")

        self.assertEqual(user.wallet_balance, 0)

    def test_load_wallet(self):
        user = User("Lone Voyager")
        user.load_wallet(500)

        self.assertEqual(user.wallet_balance, 500)

    def test_balance_after_travels(self):
        user = User("Lone Voyager")

        abuja = Station("Abuja", "natural", "earth")
        spock = Station("Spock", "natural", "mars")
        iss = Station("ISS", "manmade", "earth")
        moon = Station("Abuja", "natural", "earth")

        falcon_1 = Rocket("Falcon 1", False)
        falcon_9 = Rocket("Falcon 9", True)

        # load the wallet with 3000BTC
        user.load_wallet(3000)
        # take trips
        user.travel(abuja, moon, falcon_9)
        user.travel(moon, spock, falcon_1)
        user.travel(spock, iss, falcon_9)

        self.assertEqual(user.wallet_balance, 1950)


if __name__ == "__main__":
    unittest.main()
