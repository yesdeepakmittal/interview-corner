#https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 0:
            n = n & (n - 1)
            cnt += 1
        return cnt