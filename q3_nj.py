import numpy as np

def NJ(name):
	if(not(name.endswith(".txt"))):
		name += ".txt"
	file = open(name, 'r')
	txt = file.read()
	
	mx = matrix(txt)
	qmx = qmatrix(txt)
	
	#adding rowsums to mx
	for i in range(1, len(mx)):
		s = 0
		for j in range(1, len(mx[i])):
			mx[i][j] = int(mx[i][j])
			s += mx[i][j]
		mx[i].append(int(s))

	calculate_qs(qmx, mx, len(mx) - 1)

	n = 0
	print_stage(mx, qmx, n)

	while (len(mx) - 1) > 2:
		n += 1
		lq = lowest_q(qmx)
		
		cluster(lq[0], lq[1], mx, qmx)
		merge(lq[0], lq[1], qmx)
		calculate_qs(qmx, mx, len(mx) - 1)
		
		print_stage(mx, qmx, n)

def col(a, mx):
	for i in range(len(mx[0])):
		if(mx[0][i] == a):
			return i

def row(a, mx):
	for i in range(1, len(mx)):
		if(mx[i][0] == a):
			return i

def d(a, b, mx):
	return mx[row(a, mx)][col(b, mx)]

def merge(a, b, mx):
	bD = {}
	ab = a + b

	#renaming column a to ab
	for i in range(len(mx[0])):
		if(mx[0][i] == a):
			mx[0][i] = ab
			break

	iB = col(b, mx)

	# removing row b and caching the d values
	c = 0
	for i in range(1, len(mx)):
		#renaming row a
		if(mx[i][0] == a):
			mx[i][0] = ab
		
		bD[mx[i][0]] = mx[i][iB]
		mx[i].pop(iB)

	mx.pop(row(b, mx))
	mx[0].remove(b)

	bD[a] = bD[ab]
	del bD[ab]
	
	return bD

# merges + recalculates the matrix
def cluster(a, b, mx, qmx):
	ab = a + b
	cache = merge(a, b, mx)

	# new distance values
	rowAB = row(ab, mx)
	for j in range(1, len(mx[rowAB]) - 1):
		c = mx[0][j]
		if(c == ab):
			mx[rowAB][j] = 0
			continue
		
		v = (d(ab, c, mx) + cache[c] - cache[a]) / 2
		mx[rowAB][j] = v
		mx[j][rowAB] = v

	#updates the row sums
	for i in range(1, len(mx)):
		mx[i][-1] = sum(mx[i][1:-1])

# fills the q matrix 
def calculate_qs(qmx, mx, r):
	c = 2
	for i in range(1, len(qmx)):
		for j in range(c, len(qmx[i])):
			qmx[i][j] = Q(qmx[i][0], qmx[0][j], r, mx)
		c += 1

# finds the lowest q value in the q matrix
def lowest_q(qmx):
	lowestQ = None
	lowestP = None

	c = 2
	for i in range(1, len(qmx)):
		for j in range(c, len(qmx[i])):
			q = qmx[i][j]
			if(lowestQ == None or lowestQ > q):
				lowestQ = q
				lowestP = (qmx[i][0], qmx[0][j])
		c += 1

	return lowestP

# calculates Q value of an a and b
def Q(a, b, r, mx):
	for i in mx:
		if(i[0] == a):
			rA = i[-1]
		if(i[0] == b):
			rB = i[-1]

	return (r - 1) * d(a, b, mx) - rA - rB

# util to print matrix
def print_matrix(mx):
	print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in mx]))

# util to create matrix from text
def matrix(dat):
	mx = []
	a = dat.split("\n")
	for i in a:
		row = []
		for j in i.split(" "):
			row.append(j)
		mx.append(row)
	return mx

# removed distance values from the matrix to make it a 'q matrix'
def qmatrix(dat):
	mx = matrix(dat)
	for i in range(1, len(mx)):
		for j in range(1, len(mx[i])):
			mx[i][j] = '-'
	return mx

# prints all required info of a NJ stage
def print_stage(mx, qmx, n):
	print("------ n = "+ str(n) + ": ------")
	print_matrix(mx)
	print(" ")
	print("Q-matrix: ")
	print_matrix(qmx)
	print(" ")
