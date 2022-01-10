class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        def fact(n):
            if n == 1:
                return 1
            return n*fact(n-1)
        return fact(A)
