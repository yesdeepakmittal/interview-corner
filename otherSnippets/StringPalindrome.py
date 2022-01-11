class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        d = {}
        for i in A:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        one = 0
        for k,v in d.items():
            if v%2 != 0:
                one += 1
        if one == 1 or one == 0:
            return 1
        return 0

A = 'abbaee'
print(Solution().solve(A)) 