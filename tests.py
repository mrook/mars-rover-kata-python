import unittest
from rover import Rover

class RoverTest(unittest.TestCase):
    def test_exception_for_unknown_command(self):
        rover = Rover()
        with self.assertRaises(Exception):
            rover.process_command('X')


if __name__ == '__main__':
    unittest.main()
