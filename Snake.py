from Cell import Cell

class Snake:

	# must pass a valid list of Cells with at least one cell (the head)
	# must pass a valid direction ('up', 'down', 'left', 'right')
	def __init__(self, cell_list, direction):
		self.cell_list = cell_list
		self.direction = direction


	##########################################################
	###########              FUNCTIONS            ############
	##########################################################


	# moves snake in its current direction by moving head in 
	# that direction by dist, and each body cell follows
	# the one ahead of it. Returns nothing
	def move_snake(self, dist):
		
		cells = self.cell_list
		num_cells = len(cells)
		
		if num_cells > 1:
			# make each body cell follow one ahead of it
			# (loop starting from tail cell going up to head)
			for i in reversed(range(1, num_cells)):
				cells[i].coord = cells[i-1].coord

		# move head in current snake direction
		dir = self.direction 	 
		cells[0].move_cell(dir, dist) 

	# adds a cell to end of snake body. Returns nothing
	def add_cell(self, coord, cell_size):
		new_cell = Cell(coord)
		self.cell_list.append(new_cell)
		


