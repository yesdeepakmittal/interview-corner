class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        res = [[0 for x in range(len(B[0]))] for y in range(len(A))]

        for row in range(len(A)):
            for j in range(len(B[0])):
                for i in range(len(A[0])):
                    res[row][j] += A[row][i] * B[i][j]
        return res
