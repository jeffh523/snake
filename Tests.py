import unittest
from Snake import Snake
from Cell import Cell


class Tests(unittest.TestCase):

	# start each test with a 3-celled snake, moving left
	def setUp(self):
		self.head = Cell((50, 50))
		self.body = Cell((self.head.coord[0] + 1, self.head.coord[1]))
		self.tail = Cell((self.head.coord[0] + 2, self.head.coord[1]))
		self.cells = [self.head, self.body, self.tail] 
		self.snakey = Snake(self.cells, 'left')


	def test_move_left(self):
		# check initial cell positions
		self.assertEqual(self.snakey.cell_list[0].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[0].coord[1], 50)
		self.assertEqual(self.snakey.cell_list[1].coord[0], 50 + 1)
		self.assertEqual(self.snakey.cell_list[1].coord[1], 50)
		self.assertEqual(self.snakey.cell_list[2].coord[0], 50 + 2)
		self.assertEqual(self.snakey.cell_list[2].coord[1], 50)
		# move snake (left)
		self.snakey.move_snake()
		# check head is one cell left
		self.assertEqual(self.snakey.cell_list[0].coord[0], (50 - 1))
		self.assertEqual(self.snakey.cell_list[0].coord[1], 50)
		# check other cells followed the one ahead of them
		self.assertEqual(self.snakey.cell_list[1].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[1].coord[1], 50)
		self.assertEqual(self.snakey.cell_list[2].coord[0], 50 + 1)
		self.assertEqual(self.snakey.cell_list[2].coord[1], 50)

	def test_move_up(self):
		self.snakey.direction = 'up'
		# check initial cell positions
		self.assertEqual(self.snakey.cell_list[0].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[0].coord[1], 50)
		self.assertEqual(self.snakey.cell_list[1].coord[0], 50 + 1)
		self.assertEqual(self.snakey.cell_list[1].coord[1], 50)
		self.assertEqual(self.snakey.cell_list[2].coord[0], 50 + 2)
		self.assertEqual(self.snakey.cell_list[2].coord[1], 50)
		# move snake (up)
		self.snakey.move_snake()
		# check head is one cell up
		self.assertEqual(self.snakey.cell_list[0].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[0].coord[1], 50 - 1)
		# check other cells followed the one ahead of them
		self.assertEqual(self.snakey.cell_list[1].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[1].coord[1], 50)
		self.assertEqual(self.snakey.cell_list[2].coord[0], 50 + 1)
		self.assertEqual(self.snakey.cell_list[2].coord[1], 50)

		# move it up again
		self.snakey.move_snake()
		# check head is one cell up
		self.assertEqual(self.snakey.cell_list[0].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[0].coord[1], 50 - 2)
		# check other cells followed the one ahead of them
		self.assertEqual(self.snakey.cell_list[1].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[1].coord[1], 50 - 1)
		self.assertEqual(self.snakey.cell_list[2].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[2].coord[1], 50)

		# move it up again
		self.snakey.move_snake()
		# check head is one cell up
		self.assertEqual(self.snakey.cell_list[0].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[0].coord[1], 50 - 3)
		# check other cells followed the one ahead of them
		self.assertEqual(self.snakey.cell_list[1].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[1].coord[1], 50 - 2)
		self.assertEqual(self.snakey.cell_list[2].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[2].coord[1], 50 - 1)


	def test_move_down(self):
		self.snakey.direction = 'down'
		# check initial cell positions
		self.assertEqual(self.snakey.cell_list[0].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[0].coord[1], 50)
		self.assertEqual(self.snakey.cell_list[1].coord[0], 50 + 1)
		self.assertEqual(self.snakey.cell_list[1].coord[1], 50)
		self.assertEqual(self.snakey.cell_list[2].coord[0], 50 + 2)
		self.assertEqual(self.snakey.cell_list[2].coord[1], 50)
		# move snake (down)
		self.snakey.move_snake()
		# check head is one cell down
		self.assertEqual(self.snakey.cell_list[0].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[0].coord[1], 50 + 1)
		# check other cells followed the one ahead of them
		self.assertEqual(self.snakey.cell_list[1].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[1].coord[1], 50)
		self.assertEqual(self.snakey.cell_list[2].coord[0], 50 + 1)
		self.assertEqual(self.snakey.cell_list[2].coord[1], 50)


	def test_move_right(self):
		# for this test we need to re-orient the snake,
		# such that its body/tail is to the left of its head
		new_body = Cell((50 - 1, self.head.coord[1]))
		new_tail = Cell((50 - 2, self.head.coord[1]))
		self.snakey.cell_list = [self.head, new_body, new_tail]
		self.snakey.direction = 'right'
		# check initial cell positions
		self.assertEqual(self.snakey.cell_list[0].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[0].coord[1], 50)
		self.assertEqual(self.snakey.cell_list[1].coord[0], 50 - 1)
		self.assertEqual(self.snakey.cell_list[1].coord[1], 50)
		self.assertEqual(self.snakey.cell_list[2].coord[0], 50 - 2)
		self.assertEqual(self.snakey.cell_list[2].coord[1], 50)
		# move snake (right)
		self.snakey.move_snake()
		# check head is one cell right
		self.assertEqual(self.snakey.cell_list[0].coord[0], 50 + 1)
		self.assertEqual(self.snakey.cell_list[0].coord[1], 50)
		# check other cells followed the one ahead of them
		self.assertEqual(self.snakey.cell_list[1].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[1].coord[1], 50)
		self.assertEqual(self.snakey.cell_list[2].coord[0], 50 - 1)
		self.assertEqual(self.snakey.cell_list[2].coord[1], 50)

	def test_move_head_only(self):
		new_cells_list = [self.head]
		self.snakey.cell_list = new_cells_list
		# check initial cell position
		self.assertEqual(self.snakey.cell_list[0].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[0].coord[1], 50)
		self.assertEqual(1, len(self.snakey.cell_list))
		# move snake (left)
		self.snakey.move_snake()
		self.assertEqual(self.snakey.cell_list[0].coord[0], 50 - 1)
		self.assertEqual(self.snakey.cell_list[0].coord[1], 50)
		# move snake (up)
		self.snakey.direction = 'up'
		self.snakey.move_snake()
		self.assertEqual(self.snakey.cell_list[0].coord[0], 50 - 1)
		self.assertEqual(self.snakey.cell_list[0].coord[1], 50 - 1)
		# move up again
		self.snakey.move_snake()
		self.assertEqual(self.snakey.cell_list[0].coord[0], 50 - 1)
		self.assertEqual(self.snakey.cell_list[0].coord[1], 50 - 2)
		# move snake right
		self.snakey.direction = 'right'
		self.snakey.move_snake()
		self.assertEqual(self.snakey.cell_list[0].coord[0], 50)
		self.assertEqual(self.snakey.cell_list[0].coord[1], 50 - 2)


def main():
    unittest.main()

if __name__ == '__main__':
    main()


