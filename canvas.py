import numpy as np
from numpy import random
from termcolor import cprint


def getRandoms(width, height):
	randoms = random.randint(1, 5, size=(width * height))
	return randoms


def initializeMatrix(width, height):
	return np.zeros((height, width))


def paintCanvas(width, height):
	randoms = getRandoms(width, height)
	m = initializeMatrix(width, height)
	num = -1

	for row in range(0, height):
		for col in range(0, width):
			if m[row][col] == 0:
				num += 1
				if randoms[num] == 4:
					if col != width - 1 and row != height - 1 \
							and m[row + 1][col] == m[row][col + 1] == m[row + 1][col + 1] == 0:
						m[row][col] = m[row + 1][col] = m[row][col + 1] = m[row + 1][col + 1] = 4
					elif col == width - 1 or (col != width - 1 and m[row][col + 1] != 0):
						randoms[num] = 3
					elif row == height - 1:
						randoms[num] = 2
				if randoms[num] == 3:
					if row != height - 1:
						m[row][col] = m[row + 1][col] = 3
					elif row == height - 1 and col != width - 1 and m[row][col + 1] == 0:
						randoms[num] = 2
					elif row == height - 1 and (col == width - 1 or m[row][col + 1] != 0):
						randoms[num] = 1
				if randoms[num] == 2:
					if col != width - 1 and m[row][col + 1] == 0:
						m[row][col] = m[row][col + 1] = 2
					elif col == width - 1 or (col != width - 1 and m[row][col + 1] != 0):
						randoms[num] = 1
				if randoms[num] == 1:
					m[row][col] = 1

	return m


def printCanvas(m, width, height):
	for row in range(0, height):
		for col in range(0, width):
			if m[row][col] == 4:
				cprint(".4.", 'red', 'on_red', end="")
			if m[row][col] == 3:
				cprint(".3.", 'green', 'on_green', end="")
			if m[row][col] == 2:
				cprint(".2.", 'blue', 'on_blue', end="")
			if m[row][col] == 1:
				cprint(".1.", 'yellow', 'on_yellow', end="")
			if m[row][col] == 0:
				cprint(".0.9", 'white', 'on_white', end="")
		print()


def regenerate(width, height):
	cprint("Get a different design for the canvas? (y/n) ", 'green', end="")
	r = input()
	while(r == 'y' or r == 'Y'):
		m = paintCanvas(width, height)
		cprint("\nNEW RESULT:", 'blue')
		printCanvas(m, width, height)
		cprint("Get a different design for the canvas? (y/n) ", 'green', end="")
		r = input()


def welcome():
	cprint("This script uses shapes from the list below to fill a canvas of given dimensions.", 'blue')
	cprint("THE SHAPES:", 'blue')

	print("\t", end="")
	cprint(".4.", 'red', 'on_red', end="")
	cprint(".4.", 'red', 'on_red', end="\t")

	cprint(".3.", 'green', 'on_green', end="\t")

	cprint(".2.", 'blue', 'on_blue', end="")
	cprint(".2.", 'blue', 'on_blue', end="\t")

	cprint(".1.", 'yellow', 'on_yellow')

	print("\t", end="")
	cprint(".4.", 'red', 'on_red', end="")
	cprint(".4.", 'red', 'on_red', end="\t")

	cprint(".3.", 'green', 'on_green')

	cprint("THE CANVAS:\n\tis a matrix of a certain width and height, which you can define here: ", 'blue', end="")

	dimensions = input().split()
	width = int(dimensions[0])
	if(len(dimensions) < 2):
		height = int(input())
	else:
		height = int(dimensions[1])

	m = paintCanvas(width, height)
	cprint("THE RESULT:", 'blue')
	printCanvas(m, width, height)

	regenerate(width, height)


welcome()
