import pygame, sys
from pygame.locals import *
from Snake import Snake
from Cell import Cell 
from random import randint

FPS = 15
WIDTH = 450
HEIGHT = 450
CELL_SIZE = 15
assert (float(WIDTH) % float(CELL_SIZE) == 0), 'illogical board/cell proportions'
assert (float(HEIGHT) % float(CELL_SIZE) == 0), 'illogical board/cell proportions'
assert( (WIDTH / 2) % CELL_SIZE == 0 and (HEIGHT / 2) % CELL_SIZE == 0), 'illogical board/cell proportions'
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FOOD_COLOR = RED
BG_COLOR = WHITE
SNAKE_COLOR = BLUE

class Game:	

	# Game constructor
	# snake is a Snake object, food is a tuple (x, y) 
	# representing food coords, and is_over is a boolean
	def __init__(self, snake, food, is_over):
		self.snake = snake
		self.food = food
		self.is_over = is_over

	##########################################################
	###########              FUNCTIONS            ############
	##########################################################

	
	# Updates the game state by moving snake if not game over,
	# and by setting is_over to true if a collision has occured.
	def update(self):
		if not self.is_over:
			# keep track of last cell before moving in case we need to add cell
			last_cell = self.snake.cell_list[len(self.snake.cell_list) -1]
			
			self.snake.move_snake(CELL_SIZE)
			
			# re-locate food if eaten
			if self.snake.cell_list[0].coord == self.food:
				self.food = get_random_coord(CELL_SIZE, WIDTH, HEIGHT)
				# make sure new food isn't on top of snake
				while self.is_food_on_snake():
					self.food = get_random_coord(CELL_SIZE, WIDTH, HEIGHT)
				# now add a cell to end of snake, where last one was before move
				self.snake.add_cell(last_cell.coord, CELL_SIZE)
			if self.is_collision():
				self.is_over = True


	# Returns True if the current state of the game involves a collision
	# (ie. the snake has hit the board edge or its own tail). Else False.
	def is_collision(self):
		return (self.snake_collision() or self.wall_collision())

	# Returns True if the current state of the game involves the snake 
	# colliding with its own body. Else False
	def snake_collision(self):
		head_coord = self.snake.cell_list[0].coord

		for i in range(1, len(self.snake.cell_list)):
			if head_coord == self.snake.cell_list[i].coord:
				return True
		return False

	# Returns true if the current state of the game involves the snake
	# colliding with the board edge. Else False
	def wall_collision(self):
		left = 0 
		right = WIDTH
		top = 0
		bottom = HEIGHT
		headx = self.snake.cell_list[0].coord[0]
		heady = self.snake.cell_list[0].coord[1]

		return (headx < left or headx >= right or heady < top or heady >= bottom)
			

	# Returns True if game's food is on top of snake
	def is_food_on_snake(self):
		for cell in self.snake.cell_list:
			if cell.coord == self.food:
				return True
		return False

	# Renders the game in its current state by calling render_snake,
	# render_border, and render_food
	def render(self, surface):
		self.render_snake(surface)
		self.render_border(surface)
		self.render_food(surface)

	# Renders the snake onto surface by drawing each snake cell
	def render_snake(self, surface):
		for cell in self.snake.cell_list:
			# draw the cell Rect object
			x = cell.coord[0]
			y = cell.coord[1]
			cell_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
			pygame.draw.rect(surface, SNAKE_COLOR, cell_rect) 
			# draw a border around the cell.
			top_left = cell.coord
			bot_left = (cell.coord[0], cell.coord[1] + CELL_SIZE)
			top_right = (cell.coord[0] + CELL_SIZE, cell.coord[1])
			bot_right = (cell.coord[0] + CELL_SIZE, cell.coord[1] + CELL_SIZE)
			border_coords = [bot_left, top_left, top_right, bot_right]
			pygame.draw.lines(surface, BLACK, True, border_coords)

	# renders the borders around endge of board
	def render_border(self, surface):
		top_left = (0, 0)
		bot_left = (0, HEIGHT)
		top_right = (WIDTH, 0)
		bot_right = (WIDTH, HEIGHT)
		border_coords = [bot_left, top_left, top_right, bot_right]
		pygame.draw.lines(surface, BLACK, True, border_coords)		

	# renders the food
	def render_food(self, surface):
		food_rect = pygame.Rect(self.food, (CELL_SIZE, CELL_SIZE))			
		pygame.draw.rect(surface, FOOD_COLOR, food_rect)
		pygame.draw.lines(surface, BLACK, True, [food_rect.bottomleft, food_rect.topleft,
			food_rect.topright, food_rect.bottomright])

	# handles the game's possible key events (up, down, left, right, esc)
	def handle_key(self, event):
		# handle key up
		if event.key == K_UP or event.key == K_w:
			self.handle_key_up()
		# handle key down
		if event.key == K_DOWN or event.key == K_s:
			self.handle_key_down()
		# handle key left
		if event.key == K_LEFT or event.key == K_a:
			self.handle_key_left()
		# handle key right
		if event.key == K_RIGHT or event.key == K_d:
			self.handle_key_right()
		elif event.key == K_ESCAPE:
			pygame.quit()
			sys.exit()

	# sets snake direction to 'up', unless currently 'down'
	def handle_key_up(self):
		if self.snake.direction != 'down':
			self.snake.direction = 'up'

	# sets snake direction to 'down', unless currently 'up'
	def handle_key_down(self):
		if self.snake.direction != 'up':
			self.snake.direction = 'down'

	# sets snake direction to 'left', unless currently 'right'
	def handle_key_left(self):
		if self.snake.direction != 'right':
			self.snake.direction = 'left'

	# sets snake direction to 'right', unless currently 'left'
	def handle_key_right(self):
		if self.snake.direction != 'left':
			self.snake.direction = 'right'


def main():

	# place snake head in middle of board to start.
	#               ***  NOTE  ***
	# A cell's coord refers to its top-left-most pixel.
	# EG: a snake cell in the top-right corner of the screen 
	# has a coord of: ((WIDTH - CELL_SIZE, 0))
	head = Cell((WIDTH / 2, HEIGHT / 2))
	bod1 = Cell((WIDTH / 2 + CELL_SIZE, HEIGHT / 2))
	snake = Snake([head, bod1], 'left')
	food =  get_random_coord(CELL_SIZE, WIDTH, HEIGHT)
	game = Game(snake, food, False)

	pygame.init()
	# global FPSCLOCK, DISPLAYSURF
	FPSCLOCK = pygame.time.Clock()
	# The display surface object:
	DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('snake')


	# MAIN GAME LOOP
	while True:		

		# var to stop more than one key event per frame
		key_pressed = False

		# Event Handling
		for event in pygame.event.get():
			
			# handle Exit
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			# handle keypress
			elif event.type == KEYDOWN:
				if not key_pressed:
					game.handle_key(event)  # gives snake direction
					key_pressed = True	

		# update game state
		game.update()

		# draw new game state
		DISPLAYSURF.fill(BG_COLOR)  
		game.render(DISPLAYSURF)

		pygame.display.update()
		FPSCLOCK.tick(FPS)		


# Returns a tuple (x, y) generated randomly
# such that x and y are multiples of cell_size
# and fall within width and height
def get_random_coord(cell_size, width, height):
	low_bound_x = 0
	hi_bound_x = width - cell_size
	mid_x = (low_bound_x + hi_bound_x) / 2
	
	# pick a random x within board dimensions
	x = randint(low_bound_x, hi_bound_x)
	#ensure x is a multiple of cell_size
	gap = x % cell_size
	if gap != 0:
		x -= gap

	low_bound_y = 0
	hi_bound_y = height - cell_size
	mid_y = (low_bound_y + hi_bound_y) / 2 

	# pick a random y within board dimensions
	y = randint(low_bound_y, hi_bound_y)
	#ensure y is a multiple of cell_size
	gap = y % cell_size
	if gap != 0:
		y -= gap

	return (x, y)




if __name__ == '__main__':
	main()


