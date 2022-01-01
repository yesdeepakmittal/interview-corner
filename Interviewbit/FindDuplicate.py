class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        # s = sum(A)
        ans = 0
        d = {}
        for i in A:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i,j in d.items():
            if j == 2:
                return i
        return -1