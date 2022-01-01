class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        for row in range(len(A)):
            for col in range(len(A[0])):
                A[row][col] = A[row][col] - B[row][col]
        return A