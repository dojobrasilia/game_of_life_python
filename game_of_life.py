class GameOfLife(object):
  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.board = self.createBoard()
    pass

  def dimensions(self):
    return [self.rows,self.cols]

  def createBoard(self):
    result = ""
    for x in range(0,self.rows):
      for y in range(0,self.cols):
        result += " "
      result += "\n"  
    return result

  def setAlive(self,row,col):
    lines = self.board.split("\n") 
    print(lines[col])
    lines[col-1] = "x"
    self.board = "\n".join(lines)
    pass


