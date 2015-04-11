import unittest
from game_of_life import GameOfLife

class game_of_life_test(unittest.TestCase):

  def test_we_have_a_game(self):
    game = GameOfLife(0,0)
    self.assertEquals(game.dimensions(),[0,0])

    game = GameOfLife(1,1)
    self.assertEquals(game.dimensions(),[1,1])


  def test_linha_morta (self):
    game = GameOfLife(1,2)
    self.assertEquals(game.board(),
      [[0,0]]
    )

  def test_multilinha_morta (self):
    game = GameOfLife(2,1)
    self.assertEquals(game.board(),
      [[0],[0]]
    )
