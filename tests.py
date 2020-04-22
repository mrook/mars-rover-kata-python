import unittest
from rover import Rover
from position import Position


class RoverTest(unittest.TestCase):
    def test_rover_returns_position_and_facing(self):
        rover = Rover(Position(1, 2), 'N')
        self.assertEqual(rover.get_position().x, 1)
        self.assertEqual(rover.get_position().y, 2)
        self.assertEqual(rover.get_direction(), 'N')

    def test_exception_for_unknown_command(self):
        rover = Rover(Position(1, 2), 'N')
        with self.assertRaises(Exception):
            rover.process_command('X')


if __name__ == '__main__':
    unittest.main()
