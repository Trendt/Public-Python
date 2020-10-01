from gameboard import Gameboard
from sys import exit

gb = Gameboard()
game_running = True
turn = 2

def ask_move():
    from_field = list(map(int,input("From field: ").split()))
    to_field = list(map(int,input("To field: ").split()))
    
    if turn == 1:
        for fig in gb.p1.figures:
            if fig.current_pos == from_field:
                fig.current_pos = to_field
    else:
        for fig in gb.p2.figures:
            if fig.current_pos == from_field:
                fig.current_pos = to_field
                
                
if __name__ == "__main__":
    while game_running:
        turn = 2 if turn == 1 else 1
        gb.render_board()
        if turn == 1:
            print(gb.p1.figures[0].color + f"Player {turn} turn" + "\x1b[0m")
        else:
            print(gb.p2.figures[0].color + f"Player {turn} turn" +"\x1b[0m")
        ask_move()
        