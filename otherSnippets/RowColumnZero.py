class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        idx = []
        for row in range(len(A)):
            for index,value in enumerate(A[row]):
                if value == 0:
                    A[row] = [0 for i in range(len(A[row]))]
                    idx.append(index)
                    # break
        for i in idx:
            for row in range(len(A)):
                A[row][i] = 0
        return A

