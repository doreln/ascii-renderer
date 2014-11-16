import time
import random
#blocks = [[[1,1,1],[1,1,1],[1,1,1]],[[1,1,1],[1,1,0],[1,0,0]],[[1,1,0],[1,0,0],[0,0,0]],[[1,0,0],[0,0,0],[0,0,0]]]
blocks = [[[0 for y in range(4)] for x in range(8)] for z in range(10)]
#blocks = [[[0,0,1],[0,0,0],[1,0,0]], [[1,1,1],[1,0,0],[1,1,0]],[[1,1,1],[1,0,1],[1,0,0]],[[0,0,0],[0,0,2],[0,0,0]],[[2,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[2,0,0]],[[0,0,0],[0,0,2],[0,0,0]],[[0,0,0],[0,2,0],[0,0,0]]]
canvas = [[" " for x in range(79)] for y in range(30)]
X = 40
Y = 20


def draw(blocks, canvas, t, order):
	clear(canvas)
	#print "z is up, x is right, y is diagonal"
	# (0, 0, 0) is the coordinate furthest away
	print "t =", t, "out of 10"
	for x,y,z in order:
		if blocks[z][x][y]:
			YY = Y - 2 * z + y
			XX = X - 3 * x + 2 * y

			if blocks[z][x][y] == 1:
				if canvas[YY][XX] == " ":
					canvas[YY][XX] = "_"     #str(i)
				if canvas[YY][XX + 1] == " ":
					canvas[YY][XX + 1] = "_"
				if canvas[YY][XX + 2] == " ":
					canvas[YY][XX + 2] = "_"

				canvas[YY + 1][XX - 1] = "|"
				canvas[YY + 1][XX] = "\\"
				canvas[YY + 1][XX + 1] = "_"
				canvas[YY + 1][XX + 2] = "_"
				canvas[YY + 1][XX + 3] = "\\"

				canvas[YY + 2][XX - 1] = "|"
				canvas[YY + 2][XX]     = " "
				canvas[YY + 2][XX + 1] = "|"

				canvas[YY + 2][XX + 2] = " "
				canvas[YY + 2][XX + 3] = " "
				canvas[YY + 2][XX + 4] = "|"

				canvas[YY + 3][XX]     = "\\"
				canvas[YY + 3][XX + 1] = "|"
				canvas[YY + 3][XX + 2] = "_"
				canvas[YY + 3][XX + 3] = "_"
				canvas[YY + 3][XX + 4] = "|"
			else:
				eye = "^"
				if random.random() > 0.9:
					eye = "*"
				canvas[YY + 2][XX + 0] = eye
				canvas[YY + 2][XX + 1] = "_"
				canvas[YY + 2][XX + 2] = eye

def getSortedCoordinates(blocks):
	X, Y, Z = len(blocks[0]), len(blocks[0][0]), len(blocks)
	mylist = [(x,y,z) for z in range(Z) for y in range(Y) for x in range(X)]
	mylist.sort(key = sum)
	return mylist


def physics(blocks):
	for y in range(len(blocks[0][0])):
		for x in range(len(blocks[0])):
			for z in range(len(blocks) - 1):
				if blocks[z+1][x][y]:
					if not blocks[z][x][y]:
						blocks[z][x][y] += blocks[z+1][x][y]
						blocks[z + 1][x][y] = 0

def clear(canvas):
	nlines = len(canvas)
	length = len(canvas[0])
	for i in range(nlines):
		for j in range(length):
			canvas[i][j] = " "

def display(canvas):
	temp = ""
	for line in canvas:    
		for string in line:
			temp += string
		temp += "\n"
	print temp

def randomize(blocks):
	for y in range(len(blocks[0][0])):
		for x in range(len(blocks[0])):
			for z in range(len(blocks)):
				r = random.random()
				if r > 0.9:
					blocks[z][x][y] = 1
				elif r < 0.02:
					blocks[z][x][y] = 2
				else:
					blocks[z][x][y] = 0

randomize(blocks)
order = getSortedCoordinates(blocks)
for t in range(1, 11):
	draw(blocks, canvas, t, order)
	display(canvas)
	physics(blocks)
	time.sleep(0.1)