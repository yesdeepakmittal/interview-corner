'''
Two arrays A & B of size M & N respectively

find common element such that each element occurs same number of times in each array
A = [1, 2, 2, 1]
B = [2, 3, 1, 2]
[1, 2, 2]

A = [2, 1, 4, 10]
B = [3, 6, 2, 10, 10]
[2, 10]
'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        a = {}
        b = {}
        for i in A:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        
        for i in B:
            if i in b:
                b[i] += 1
            else:
                b[i] = 1
        ans = []
        for key in a:
            if a.get(key) and b.get(key):
                mn = min(a.get(key),b.get(key))
                for i in range(mn):
                    ans.append(key)
        return ans
