from player import Player

class Gameboard():
    def __init__(self):
        self.game_board = []
        self.p1 = Player()
        self.p2 = Player(2)
        self.none_field = "  "
        
        self.create_board()
        self.add_figures()
        
    def render_board(self):
        self.update_figures()
        row_str = "#   " + "   #   ".join(map(str,self.game_board[0])) + "   #"
        print(len(8*"#        " + "#")*"#")
        for row in self.game_board:
            row_str = "#   " + "   #   ".join(map(str,row)) + "   #"
            
            print(8*"#        " + "#")
            print(row_str)
            print(8*"#        " + "#")
            print(len(8*"#        " + "#")*"#")
        
    def update_figures(self):
        self.game_board = []
        self.create_board()
        self.add_figures()
        
    def create_board(self):
        for x in range(8):
            row = []
            for y in range(8):
                row.append(self.none_field)
            self.game_board.append(row)
            
    def add_figures(self):
        for figure in self.p1.figures:
            self.game_board[figure.current_pos[1]][figure.current_pos[0]] = figure
        for figure in self.p2.figures:
            self.game_board[figure.current_pos[1]][figure.current_pos[0]] = figure