from pathlib import Path
import sys

class figure():
    def __init__(self,x_start:int,y_start:int,figure_name:str,figure_value:int,image_path:str="", color:str="black"):
        self.start_pos = [x_start,y_start]
        self.current_pos = self.start_pos
        self.ever_moved = False
        self.name = figure_name
        self.value = figure_value
        self.alive = True
        self.image_path = Path(image_path)
        self.color = "\x1b[1;48;30m" if color == "black" else "\x1b[1;37;40m" 
        
    def __str__(self):
        return self.color + self.name[:2].capitalize() + "\x1b[0m"
        
    def died(self):
        self.alive = False
        
    def move(self,target_x,target_y):
        self.current_pos = [target_x,target_y]
    
class Pawn(figure):
    def __init__(self, x_start, y_start,image_path,color):
        super().__init__(x_start, y_start,"pawn",1,image_path,color)
        
    def __str__(self):
        return super().__str__()
        
class King(figure):
    def __init__(self, x_start, y_start,image_path,color):
        super().__init__(x_start, y_start, "king",0,image_path,color)
        
    def __str__(self):
        return super().__str__()
        
class Queen(figure):
    def __init__(self, x_start, y_start,image_path,color):
        super().__init__(x_start, y_start, "queen",9,image_path,color)
        
    def __str__(self):
        return super().__str__()
        
class Rook(figure):
    def __init__(self, x_start, y_start,image_path,color):
        super().__init__(x_start, y_start, "rook",5,image_path,color)
        
    def __str__(self):
        return super().__str__()
        
class Bishop(figure):
    def __init__(self, x_start, y_start,image_path,color):
        super().__init__(x_start, y_start, "bishop",3,image_path,color)
        
    def __str__(self):
        return super().__str__()
        
class Knight(figure):
    def __init__(self, x_start, y_start,image_path,color):
        super().__init__(x_start, y_start, "knight",3,image_path,color)
        
    def __str__(self):
        return super().__str__()