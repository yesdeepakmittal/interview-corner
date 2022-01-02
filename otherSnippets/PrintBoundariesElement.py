'''
Print elements which are at boundaries in clock-wise

o/p = 1 -> 25
'''
if __name__ == "__main__":
	# Your code goes here
	mat = [[1,2,3,4,5],
		  [15,24,25,20,7],
		  [16,17,18,19,6],
		  [14,23,22,21,8],
		  [13,12,11,10,9]]
	n = len(mat)
	i = 0
	j = 0
	inner_iter = n - 1
	for num in range(n//2):
		for k in range(inner_iter):
			print(mat[i][j])
			j += 1
		for k in range(inner_iter):
			print(mat[i][j])
			i += 1
		for k in range(inner_iter):
			print(mat[i][j])
			j -= 1
		for k in range(inner_iter):
			print(mat[i][j])
			i -= 1		
		i += 1
		j += 1
		inner_iter -= 2
	if n&1 != 0:  #if n is odd 
		print(mat[i][j])
			