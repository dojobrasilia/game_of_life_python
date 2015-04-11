class GameOfLife(object):
  def __init__(self, rows, cols):
    self.cols = cols
    self.rows = rows

  def dimensions(self):
    return [self.cols, self.rows]

  def board(self):
    linhas = []
    coluna = []
    for col in xrange(0,self.cols):
      coluna.append(0)
    for row in range(self.rows):
      linhas.append(coluna)
    return linhas

