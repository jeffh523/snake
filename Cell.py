class Cell:

	# Constructor. coord is a tuple of ints (x, y)
	def __init__(self, coord):
		self.coord = coord 

	##########################################################
	###########              FUNCTIONS            ############
	##########################################################

	
	# moves the cell up dist pixels. returns nothing
	def move_cell_up(self, dist):
		x = self.coord[0]
		new_y = self.coord[1] - dist
		new_coord = (x, new_y)
		self.coord = new_coord

	# moves the cell down dist pixels. returns nothing
	def move_cell_down(self, dist):
		x = self.coord[0]
		new_y = self.coord[1] + dist
		new_coord = (x, new_y)
		self.coord = new_coord

	# moves the cell left dist pixels. returns nothing
	def move_cell_left(self, dist):
		y = self.coord[1]
		new_x = self.coord[0] - dist
		new_coord = (new_x, y)
		self.coord = new_coord

	# moves the cell right dist pixels. returns nothing
	def move_cell_right(self, dist):
		y = self.coord[1]
		new_x = self.coord[0] + dist
		new_coord = (new_x, y)
		self.coord = new_coord

	# moves cell dist pixels in given dir. returns nothing
	def move_cell(self, dir, dist):
		if dir == 'left':
			self.move_cell_left(dist)
		elif dir == 'right':
			self.move_cell_right(dist)
		elif dir == 'up':
			self.move_cell_up(dist)
		else:
			self.move_cell_down(dist)



