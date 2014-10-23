class Cell:

	# Constructor. coord is a tuple of ints (x, y)
	def __init__(self, coord):
		self.coord = coord 

	##########################################################
	###########              FUNCTIONS            ############
	##########################################################

	
	# moves the cell up. returns nothing
	def move_cell_up(self, cell_size):
		x = self.coord[0]
		new_y = self.coord[1] - cell_size
		new_coord = (x, new_y)
		self.coord = new_coord

	# moves the cell down. returns nothing
	def move_cell_down(self, cell_size):
		x = self.coord[0]
		new_y = self.coord[1] + cell_size
		new_coord = (x, new_y)
		self.coord = new_coord

	# moves the cell left. returns nothing
	def move_cell_left(self, cell_size):
		y = self.coord[1]
		new_x = self.coord[0] - cell_size
		new_coord = (new_x, y)
		self.coord = new_coord

	# moves the cell right. returns nothing
	def move_cell_right(self, cell_size):
		y = self.coord[1]
		new_x = self.coord[0] + cell_size
		new_coord = (new_x, y)
		self.coord = new_coord

	# moves cell in given direction. returns nothing
	def move_cell(self, dir, cell_size):
		if dir == 'left':
			self.move_cell_left(cell_size)
		elif dir == 'right':
			self.move_cell_right(cell_size)
		elif dir == 'up':
			self.move_cell_up(cell_size)
		else:
			self.move_cell_down(cell_size)



