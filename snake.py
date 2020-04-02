import time
import random
import keypoller as keys

height = 40
width = 40

delay = 0.1 # seconds

ascart = ('┛', '┗', '┃', '━', '┏', '┓', '▉', '▲')
top_row = '\n' + ascart[4] + ascart[3] * width + ascart[5] + '\n'
bottom_row = ascart[1] + ascart[3] * width + ascart[0]

snake = [[5, 2]]
apple_position = [20, 20]

def edge_detection(new_position, current_position):
	x, y = new_position[0]
	new_head_position = [x, y]
	if new_head_position in current_position or not 0 <= x <= 40 or not 0 <= y <= 40:
		print("Game Over")
		quit()

def move_up(current_position): 
	new_position = [[current_position[0][0], current_position[0][1] - 1]] + current_position[: -1]
	edge_detection(new_position, current_position)
	return new_position

def move_down(current_position):
	new_position = [[current_position[0][0], current_position[0][1] + 1]] + current_position[: -1]
	edge_detection(new_position, current_position)
	return new_position

def move_left(current_position):
	new_position = [[current_position[0][0] - 1, current_position[0][1]]] + current_position[: -1]
	edge_detection(new_position, current_position)
	return new_position

def move_right(current_position):
	new_position = [[current_position[0][0] + 1, current_position[0][1]]] + current_position[: -1]
	edge_detection(new_position, current_position)
	return new_position


def build_buffer(position):
	screen = top_row
	for j in range(height):
		screen += ascart[2]
		for i in range(width):
			if [i, j] in position:
				screen += ascart[6]
			elif [i, j] == apple_position:
				screen += ascart[7]
			else:
				screen += ' '
		screen += ascart[2] + '\n'
	screen += bottom_row
	return screen


def grow(position):
	position.append(position[:-1])
	return position

def move_apple():
	apple_position[0] = random.randint(0, 39)
	apple_position[1] = random.randint(0, 39)


# snake = handle_down(5, snake)
# snake = handle_right(10, snake)
# snake = handle_down(20, snake)
# print(apple_position)

direction = 'right'
while True:
	key = keys.listen_on_sleep(0.075)
	if key == 'return':
		quit()
	if key != direction and not key is None:
		direction = key
	if direction == 'right':
		snake = move_right(snake)
		print(build_buffer(snake))
		if snake[0] == apple_position:
			snake = grow(snake)
			move_apple()
	elif direction == 'left':
		snake = move_left(snake)
		print(build_buffer(snake))
		if snake[0] == apple_position:
			snake = grow(snake)
			move_apple()
	elif direction == 'up':
		snake = move_up(snake)
		print(build_buffer(snake))
		if snake[0] == apple_position:
			snake = grow(snake)
			move_apple()
	elif direction == 'down':
		snake = move_down(snake)
		print(build_buffer(snake))
		if snake[0] == apple_position:
			snake = grow(snake)
			move_apple()
































