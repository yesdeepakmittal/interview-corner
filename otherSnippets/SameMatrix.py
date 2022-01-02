class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        for row in range(len(A)):
            for col in range(len(A[row])):
                if A[row][col] != B[row][col]:
                    return 0
        return 1
