''''
i/p = [[1,2,3,4,5],
       [11,22,33,44,55],
       [1111,2222,3333,4444,5555],
       [1,2,3,4,5],
       [1,2,3,4,5]]
O/p - [[1, 1, 1111, 11, 1], 
       [2, 2, 2222, 22, 2], 
       [3, 3, 3333, 33, 3], 
       [4, 4, 4444, 44, 4], 
       [5, 5, 5555, 55, 5]]
'''

if __name__ == "__main__":
	# Rotate the matrix by 90 degree clockwise
	class Matrix:
		def square(self,mat):
			n = len(mat)
			m = len(mat[0])
			for row in range(n):
				for col in range(row,m):
					mat[row][col],mat[col][row] = mat[col][row],mat[row][col]
			return mat
		
		def rectangular(self,mat):
			n = len(mat)
			m = len(mat[0])
			B = [[0 for x in range(m)] for y in range(n)]
			for row in range(n):
				for col in range(m):
					B[row][col] = mat[col][row]
			return B
		
		def reverse(self,arr):
			start = 0
			end = len(arr)-1
			while start <= end:
				arr[start],arr[end] = arr[end],arr[start]
				start += 1
				end -= 1
			return arr
	
	
	mat =  [[1,2,3,4,5],
			[11,22,33,44,55],
			[1111,2222,3333,4444,5555],
			[1,2,3,4,5],
			[1,2,3,4,5]]
	mt = Matrix()
	if len(mat) == len(mat[0]):
		mat = mt.square(mat)
	else:
		mat = mt.rectangular(mat)
	for row in range(len(mat)):
		mat[row] = mt.reverse(mat[row])
	print(mat)