import unittest
from game_of_life import GameOfLife


class game_of_life_test(unittest.TestCase):

  def test_we_have_a_game(self):
    game = GameOfLife(2,1)
    self.assertEquals(game.dimensions(), [2,1])

  def test_the_simplest_game_is_only_a_dead_cell(self):
    game = GameOfLife(1,1)
    self.assertEquals(game.board," \n")  

  def test_the_simplest_game_is_only_a_dead_row(self):
    game = GameOfLife(1,2)
    self.assertEquals(game.board,"  \n")  

  def test_the_game_starts_with_a_complete_dead_board(self):
    game = GameOfLife(2,2)
    self.assertEquals(game.board,"  \n  \n") 

  def test_the_simplest_game_is_only_a_live_cell(self):
    game = GameOfLife(1,1)
    game.setAlive(1,1);
    self.assertEquals(game.board,"x\n")    

  def test_the_simplest_game_is_only_a_live_cell(self):
    game = GameOfLife(2,2)
    game.setAlive(1,1);
    self.assertEquals(game.board,"x \n  ")       