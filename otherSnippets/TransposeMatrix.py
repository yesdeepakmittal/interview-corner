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
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, mat):
        N = len(mat)
        M = len(mat[0])
        mat2 = [[0 for i in range(N)] for j in range(M)]
        for row in range(M):
            for col in range(N):
                mat2[row][col] = mat[col][row]
        return mat2

