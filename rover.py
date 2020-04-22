from position import Position


class Rover:
    def __init__(self, position: Position, direction: str):
        self.position = position
        self.direction = direction

    def process_command(self, cmd: str):
        raise Exception('Unknown command: ' + cmd)

    def get_position(self) -> Position:
        return self.position

    def get_direction(self) -> str:
        return self.direction
