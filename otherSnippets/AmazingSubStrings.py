''''
Amazing substring is one which starts with a vowel

i/p - ABEC
A | AB | ABE | ABEC | E | EC -> 6
'''
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        A = A.upper()
        l = list('AEIOU')
        n = len(A)
        cnt = 0
        for i in range(n):
            if A[i] in l:
                cnt += n - i
        return cnt % 10003
