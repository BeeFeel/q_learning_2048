from game.utils import Direction
from enum import Enum
import random
import itertools

class Game():
    X_SIZE = 4
    Y_SIZE = 4
    INIT_NUM = 1
    EMPTY = 0

    def __init__(self, is_print=False):
        self.board = [[0] * Game.X_SIZE for i in range(Game.Y_SIZE)]
        self._move_num = 0
        self._is_print = is_print
        
        # ゲーム板の初期化
        self.board[0][0] = Game.INIT_NUM

    def move(self, direction):
        x_list = [x for x in range(Game.X_SIZE)]
        y_list = [y for y in range(Game.Y_SIZE)]
        if direction == Direction.Right:
            x_list.reverse()
        if direction == Direction.Down:
            y_list.reverse()
        
        for y in y_list:
            for x in x_list:
                self._move_one(x, y, direction)

        if self._is_gameover():
            if self._is_print:
                print("GAME OVER")
                print("MAX: {}".format(self._get_maxnum()))
                print("Num of Move: {}".format(self._move_num))
            return False

        self._random_set()
        self._move_num += 1
        if self._is_print:
            self.print()
        return True

    def print(self):
        for bb in self.board:
            for b in bb:
                print("{:>5} ".format(b if b != Game.EMPTY else ""), end="")
            print()
        print("--------------------------")

    def _move_one(self, x, y, direction: Direction):
        dx, dy = Direction.to_2axiz(direction)
        if x+dx < 0 or y+dy < 0 or x+dx >= Game.X_SIZE or y+dy >= Game.Y_SIZE:
            return

        curr_ = self.board[y][x]
        next_ = self.board[y+dy][x+dx]

        if next_ == Game.EMPTY or curr_ == next_:
            self.board[y][x] = Game.EMPTY
            self.board[y+dy][x+dx] += curr_
        if next_ == Game.EMPTY:
            self._move_one(x+dx, y+dy, direction)

    def _random_set(self):
        x = random.randrange(Game.X_SIZE)
        y = random.randrange(Game.Y_SIZE)

        # 無限ループ対策
        i = 0
        while self.board[y][x] != Game.EMPTY and i < 100:
            x = random.randrange(Game.X_SIZE)
            y = random.randrange(Game.Y_SIZE)
            i += 1

        if i < 100:
            self.board[y][x] = Game.INIT_NUM

    def _is_gameover(self):
        def _can_move(board, x, y):
            for direction in Direction:
                dx, dy = Direction.to_2axiz(direction)
                if x+dx < 0 or y+dy < 0 or x+dx >= Game.X_SIZE or y+dy >= Game.Y_SIZE:
                    continue
                if board[y+dy][x+dx] == Game.EMPTY or board[y+dy][x+dx] == board[y][x]:
                    #print("{}+{}, {}+{}:".format(x, dx, y, dy), board[y+dy][x+dx], board[y][x])
                    return True
            return False
        for x, y in itertools.product(range(Game.X_SIZE), range(Game.Y_SIZE)):
            if _can_move(self.board, x, y):
                return False
        return True

    def _get_maxnum(self):
        return max(max(b for b in self.board))