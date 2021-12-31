if __name__ == "__main__":
	# Your code goes here
	mat =  [[1,2,3,4,5],
			[1,2,3,4,5],
			[1,2,3,4,5],
			[1,2,3,4,5]]

	n = len(mat)
	m = len(mat[0])

	#all diagonal from right to left
	for k in range(m):
		i = 0
		j = k
		while i < n and j >= 0:
			# print(mat[i][j])
			i += 1
			j -= 1
	for k in range(1,n):
		i = k
		j = m-1
		while i<n and j >= 0:
			print(mat[i][j])
			i += 1
			j -= 1