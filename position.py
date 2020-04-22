class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
