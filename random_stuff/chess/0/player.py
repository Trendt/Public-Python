from figures import Pawn,Bishop,King,Knight,Queen,Rook

class Player():
    def __init__(self,player_number:int=1):
        self.figures = []
        self.player_number = player_number
        self.alive = True
        self.add_figures()
        
    def add_figures(self):
        #Pawns:
        for x in range(8):
            if self.player_number == 1:
                self.figures.append(Pawn(x,1,"/src/pawn.png","white"))
            else:
                self.figures.append(Pawn(x,6,"/src/pawn.png","black"))
                
        #Rooks:
        if self.player_number == 1:
            self.figures.append(Rook(0,0,"/src/rook.png","white"))
            self.figures.append(Rook(7,0,"/src/rook.png","white"))
        else:
            self.figures.append(Rook(0,7,"/src/rook.png","black"))
            self.figures.append(Rook(7,7,"/src/rook.png","black"))
            
        #Knights:
        if self.player_number == 1:
            self.figures.append(Knight(1,0,"/src/knight.png","white"))
            self.figures.append(Knight(6,0,"/src/knight.png","white"))
        else:
            self.figures.append(Knight(1,7,"/src/knight.png","black"))
            self.figures.append(Knight(6,7,"/src/knight.png","black"))
            
        #Bishops:
        if self.player_number == 1:
            self.figures.append(Bishop(2,0,"/src/bishop.png","white"))
            self.figures.append(Bishop(5,0,"/src/bishop.png","white"))
        else:
            self.figures.append(Bishop(2,7,"/src/bishop.png","black"))
            self.figures.append(Bishop(5,7,"/src/bishop.png","black"))
            
        #Queen:
        if self.player_number == 1:
            self.figures.append(Queen(3,0,"/src/queen.png","white"))
        else:
            self.figures.append(Queen(3,7,"/src/queen.png","black"))
            
        #King:
        if self.player_number == 1:
            self.figures.append(King(4,0,"/src/king.png","white"))
        else:
            self.figures.append(King(4,7,"/src/king.png","black"))