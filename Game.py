import pygame, sys
from pygame.locals import *
from Snake import Snake
from Cell import Cell 

FPS = 15
WIDTH = 500
HEIGHT = 500
CELL_SIZE = 20
assert (float(WIDTH) % float(CELL_SIZE) == 0), 'illogical board/cell proportions'
assert (float(HEIGHT) % float(CELL_SIZE) == 0), 'illogical board/cell proportions'
CELLS_WIDE = WIDTH / CELL_SIZE
CELLS_HIGH = HEIGHT / CELL_SIZE 
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BG_COLOR = WHITE
SNAKE_COLOR = BLUE

class Game:	

	# Game constructor
	def __init__(self, snake, is_over):
		self.snake = snake
		self.is_over = is_over

	##########################################################
	###########              FUNCTIONS            ############
	##########################################################

	# renders the game in its current state by calling render_snake()
	def render(self, surface):
		self.render_snake(self.snake.direction, surface)

	# renders the snake onto surface by drawing each snake cell
	def render_snake(self, direction, surface):
		# initialize variable prev_cell
		prev_cell = None	

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
	#           ***  NOTE  ***
	# A cell's coord refers to its top-left-most pixel.
	# EG: a snake cell in the top-right corner of the screen 
	# has a coord of: ((WIDTH - CELL_SIZE, 0))
	head = Cell((WIDTH / 2, HEIGHT / 2))
	bod1 = Cell((WIDTH / 2 + CELL_SIZE, HEIGHT / 2))
	bod2 = Cell((WIDTH / 2 + (2 * CELL_SIZE), HEIGHT / 2))
	bod3 = Cell((WIDTH / 2 + (3 * CELL_SIZE), HEIGHT / 2))
	tail = Cell((WIDTH / 2 + (4 * CELL_SIZE), HEIGHT / 2))
	snake = Snake([head, bod1, bod2, bod3, tail], 'left')
	game = Game(snake, False)

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
					game.handle_key(event)
					key_pressed = True	

		DISPLAYSURF.fill(BG_COLOR)
		game.snake.move_snake(CELL_SIZE)
		game.render(DISPLAYSURF)

		pygame.display.update()
		FPSCLOCK.tick(FPS)		


if __name__ == '__main__':
	main()

