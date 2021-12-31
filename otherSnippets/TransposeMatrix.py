#Transpose Square Matrix
if __name__ == "__main__":
	# Your code goes here
	mat =  [[1,2,3,4,5],
			[1,2,3,4,5],
			[1,2,3,4,5],
			[1,2,3,4,5],
			[1,2,3,4,5]]
	for row in range(len(mat)):
		for col in range(row,len(mat[0])):
			mat[row][col],mat[col][row] = mat[col][row],mat[row][col]
	print(mat)

#Transpose Rectangular Matrix
N= 3
M = 4
