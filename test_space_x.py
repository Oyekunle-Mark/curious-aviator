import unittest
from space_x import User, Station, Rocket


class TestSpaceX(unittest.TestCase):
    def test_new_user_balance(self):
        user = User("Lone Voyager")

        self.assertEqual(user.balance, 0)


if __name__ == "__main__":
    unittest.main()
