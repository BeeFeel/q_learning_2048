from enum import Enum

class Direction(Enum):
    Up = 1
    Down = 2
    Left = 3
    Right = 4

    @classmethod
    def to_2axiz(cls, direction):
        dx, dy = (0, 0)
        if direction == Direction.Up:
            dy = -1
        elif direction == Direction.Down:
            dy = 1
        elif direction == Direction.Left:
            dx = -1
        elif direction == Direction.Right:
            dx = 1
        return dx, dy