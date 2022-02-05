'''
Magic Number -> power of 5 or sum of unique powers of 5

5, 25, 30(5 + 25), 125, 130(125 + 5), 150(125 + 25), 155(125 + 25 + 5), 625, ...

A =  3 -> 30
A = 10 -> 650

Approach:
check binary representation of a number and calculate sum by replacing 2 by 5
'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # TC - O(N) 
        var = bin(A)[2:][::-1]
        p = 1
        s = 0
        for i in var:
            if i == '1':
                s += pow(5,p)
            p += 1
        return s
    
    def solve2(self,A):
        # TC - O(logN)
        s = 0
        p = 1
        while A > 0:
            s += (A%2)*pow(5,p)
            p += 1
            A //= 2
        return s

print(Solution().solve(7))  # 155
print(Solution().solve2(7))  # 155