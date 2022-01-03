'''
Generate square matrix filled with values 1 to A2 in spiral fashion
i/p -> A = 3
o/p -> [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
'''
class Solution:
	# @param A : integer
	# @return a list of list of integers
	def generateMatrix(self, A):
		mat = [[0 for i in range(A)] for j in range(A)]
		i = 0
		j = 0
		n = 1
		inner_iter = len(mat) - 1
		for k in range(A//2):
			for var in range(inner_iter):
				mat[i][j] = n
				n += 1
				j += 1
			for var in range(inner_iter):
				mat[i][j] = n
				n += 1
				i += 1
			for var in range(inner_iter):
				mat[i][j] = n
				n += 1
				j -= 1
			for var in range(inner_iter):
				mat[i][j] = n
				n += 1
				i -= 1

			i += 1
			j += 1
			inner_iter -= 2
		if len(mat)&1 !=0:
			mat[i][j] = n
		return mat
    
print(Solution().generateMatrix(3))