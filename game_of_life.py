class GameOfLife(object):
  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    pass

  def dimensions(self):
    return [self.rows,self.cols]

  def board(self):
    result = ""
    for x in range(0,self.cols):
      result += " "
    return result + "\n"
        