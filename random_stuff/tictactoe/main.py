def refresh_board(game_board:list):
    return  ["     |     |     ",f"  {game_board[0]}  |  {game_board[1]}  |  {game_board[2]}  ","     |     |     ","-----+-----+-----",
             "     |     |     ",f"  {game_board[3]}  |  {game_board[4]}  |  {game_board[5]}  ","     |     |     ","-----+-----+-----",
             "     |     |     ",f"  {game_board[6]}  |  {game_board[7]}  |  {game_board[8]}  ","     |     |     ","     |     |     "]
    
def check_for_win(gb:list):
    gb = [None if x == " " else x for x in gb]
    gb_rows = [[gb[0],gb[1],gb[2]],
               [gb[3],gb[4],gb[5]],
               [gb[6],gb[7],gb[8]]]
               
    gb_columns = [[gb[0],gb[3],gb[6]],
                  [gb[1],gb[4],gb[7]],
                  [gb[2],gb[5],gb[8]]]
    
    gb_diagonals = [[gb[0],gb[4],gb[8]],
                    [gb[2],gb[4],gb[6]]]
    
    gb_diagonals = [list(set(x)) for x in gb_diagonals]
    gb_columns = [list(set(x)) for x in gb_columns]
    gb_rows = [list(set(x)) for x in gb_rows]
    
    for i in gb_columns:
        if len(i) == 1 and i[0] != None:
            return i[0]
        
    for j in gb_rows:
        if len(j) == 1 and j[0] != None:
            return j[0]
        
    for z in gb_diagonals:
        if len(z) == 1 and z != None:
            return z[0]
    
def game_loop():
    game_running = True
    turn = "X"
    game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    game_board_str = ["     |     |     ",f"  {game_board[0]}  |  {game_board[1]}  |  {game_board[2]}  ","     |     |     ","-----+-----+-----",
                      "     |     |     ",f"  {game_board[3]}  |  {game_board[4]}  |  {game_board[5]}  ","     |     |     ","-----+-----+-----",
                      "     |     |     ",f"  {game_board[6]}  |  {game_board[7]}  |  {game_board[8]}  ","     |     |     ","     |     |     "]

    explenation_str = ["     |     |     ","  1  |  2  |  3  ","     |     |     ","-----+-----+-----",
                       "     |     |     ","  4  |  5  |  6  ","     |     |     ","-----+-----+-----",
                       "     |     |     ","  7  |  8  |  9  ","     |     |     ","     |     |     "]

    while game_running:
        good_input = False
        while not good_input:
            try:    
                print("\n".join(game_board_str))
                print("\n")
                input_number = int(input(f"Where do you wanna go? (Player {turn}'s turn)\n" + "\n".join(explenation_str) + "\n"))
                
                if input_number > 9 or input_number < 1:
                    print("Wrong input!")
                elif game_board[input_number-1] != " ":
                    print("Field is allready full!")
                else:
                    good_input = True
                    game_board[input_number-1] = turn
                    
                winner = check_for_win(game_board)
                if winner != None:
                    game_running = False
                    
                game_board_str = refresh_board(game_board)
                turn = "O" if turn == "X" else "X"
            except Exception:
                print("Wrong input!\n")
                
    print(f"\n\nWinner is Player {winner.upper()}\n\n")
            
if __name__ == "__main__":
    game_loop()