class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        for row in range(len(A)):
            for col in range(len(A[0])):
                A[row][col] = B*A[row][col]
        return A