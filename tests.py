import unittest
from Maze import Maze
from Point import Point

class Tests(unittest.TestCase):
  def test_maze_create_cells(self):
    num_cols = 12
    num_rows = 10
    m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
    self.assertEqual(
      len(m1._cells),
      num_cols,
    )
    self.assertEqual(
      len(m1._cells[0]),
      num_rows,
    )

  def test_maze_big(self):
     num_cols = 100
     num_rows = 100
     m1 = Maze(Point(10,10), num_rows, num_cols, 10,10)
     self.assertEqual(len(m1._cells), num_cols)
     self.assertEqual(len(m1._cells[0]), num_rows)

  def test_breaking_entrance_exit(self):
     num_cols = 10
     num_rows = 10
     m1 = Maze(Point(10,10), num_rows, num_cols, 10,10)
     self.assertEqual(m1._cells[0][0].has_left_wall, False)
     self.assertEqual(m1._cells[num_cols-1][num_rows-1].has_right_wall, False)



if __name__ == "__main__":
    unittest.main()