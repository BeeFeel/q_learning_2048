import sys, termios

from game.game import Game
from game.utils import Direction

if __name__ == "__main__":
    game = Game()
    game.print()

    #標準入力のファイルディスクリプタを取得
    fd = sys.stdin.fileno()

    #fdの端末属性をゲットする
    #oldとnewには同じものが入る。
    #newに変更を加えて、適応する
    #oldは、後で元に戻すため
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)

    #new[3]はlflags
    #ICANON(カノニカルモードのフラグ)を外す
    new[3] &= ~termios.ICANON
    #ECHO(入力された文字を表示するか否かのフラグ)を外す
    new[3] &= ~termios.ECHO


    try:
        termios.tcsetattr(fd, termios.TCSANOW, new)
        # キーボードから入力を受ける。
        # lfalgsが書き換えられているので、エンターを押さなくても次に進む。echoもしない
        while True:
            ch = sys.stdin.read(1)
            if ch == "w":
                game.move(Direction.Up)
            elif ch == "a":
                game.move(Direction.Left)
            elif ch == "s":
                game.move(Direction.Down)
            elif ch == "d":
                game.move(Direction.Right)

    finally:
        termios.tcsetattr(fd, termios.TCSANOW, old)