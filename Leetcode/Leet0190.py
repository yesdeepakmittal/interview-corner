#https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]
        length = len(n)
        diff = 32 - length
        ans = '0'*diff + n
        return int(ans[::-1],base=2)