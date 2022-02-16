import numpy as np
from numpy import random
from termcolor import cprint

""" This script uses shapes from the list below to fill a canvas of given dimensions.
The shapes are: 
	⬛⬛
	⬛⬛ codded 4
	
	⬛
	⬛ codded 3
	
	⬛⬛ codded 2
	
	⬛ codded 1
	
The user enters the dimensions of the canvas.
A list of random numbers representing the codes of the shapes is created.
Parsing the list, a shape with the code coresponding the list element is 
"""

def getRandoms(width, height):														  									# function that creates a list of random numbers in the interval [1, 4]
	return random.randint(1, 5, size=(width * height))


def initializeMatrix(width, height):																					# function that initializes with values of 0 a matrix of given dimensions
	return np.zeros((height, width))


def paintCanvas(width, height):																							# function that fills the canvas using the shapes from the set
	randoms = getRandoms(width, height)																					# create a list of random numbers
	m = initializeMatrix(width, height)																					# initialize the matrix
	num = -1																											# num is used to parse the randoms list, one at a time

	for row in range(0, height):																						# parse the matrix
		for col in range(0, width):
			if m[row][col] == 0:																						# check if the cell of the matrix is empty (cell == 0)
				num += 1
				if randoms[num] == 4:																					# check if the shape that is going to be inserted is the shape codded 4
					if col != width - 1 and row != height - 1 \
							and m[row + 1][col] == m[row][col + 1] == m[row + 1][col + 1] == 0:							# check if the cell is not the last in the matrix and its E, SE and S neighbours are empty
						m[row][col] = m[row + 1][col] = m[row][col + 1] = m[row + 1][col + 1] = 4						# reinitialize the four cells with the shape's code
					elif col == width - 1 or (col != width - 1 and m[row][col + 1] != 0):								# check if the cell is on the last column or the E neighbour is not empty
						randoms[num] = 3																				# if the condition above is false, that means a 4-shape cannot be inserted. Trying now to insert a 3-shape
					# elif row == height - 1:
					# 	randoms[num] = 2
				if randoms[num] == 3:																					# check if the shape to be inserted is the shape codded 3
					if row != height - 1:																				# check if the cell is not on the last row of the matrix
						m[row][col] = m[row + 1][col] = 3																# reinitialize the cell and its S neighbour with the shape's code
					elif row == height - 1 and col != width - 1 and m[row][col + 1] == 0:								# check if the cell is on the last row but not on the last column of the matrix
						randoms[num] = 2																				# a 3-shape cannot be inserted but a 2-shape might be. Trying to insert a 2-shape
					# elif row == height - 1 and (col == width - 1 or m[row][col + 1] != 0):
					# 	randoms[num] = 1
				if randoms[num] == 2:																					# check if the shape to be inserted is the shape codded 2
					if col != width - 1 and m[row][col + 1] == 0:														# check if the cell is not on the last column of the matrix and its E neighbour is empty
						m[row][col] = m[row][col + 1] = 2																# reinitialize the cell and its E neighbour with the shape's code
					# elif col == width - 1 or (col != width - 1 and m[row][col + 1] != 0):								# check if the cell is on the last column or if the E neighbour in not empty
					# 	randoms[num] = 1																				# a 2-shape cannot be inserted. Trying to insert a 1-shape
				if randoms[num] == 1 or m[row][col] == 0:																# check if the shape to be inserted is the shape codded 1  or the cell is empty after the atempts to fill it with the code of a bigger shape
					m[row][col] = 1																						# reinitialize the cell with the shape's code

	return m


def printCanvas(m, width, height):																						# function that prints the painted canvas
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


def regenerate(width, height):																							# function that allows to get a new colouring for the defined canvas
	cprint("Get a different design for the canvas? (y/n) ", 'green', end="")
	r = input()
	while(r == 'y' or r == 'Y'):
		m = paintCanvas(width, height)
		cprint("\nNEW RESULT:", 'blue')
		printCanvas(m, width, height)
		cprint("Get a different design for the canvas? (y/n) ", 'green', end="")
		r = input()


def welcome():																											# driver function
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
