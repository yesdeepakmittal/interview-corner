#https://leetcode.com/problems/complement-of-base-10-integer/
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # ans = ''
        # n = bin(n)[2:]
        # for i in n:
        #     if i == '1':
        #         ans += '0'
        #     else:
        #         ans += '1'
        # return int(ans,base=2)
        
        import math
        if n == 0:
            return 1 #bcz math.log2(0) gives ValueError
        mask = (1 << int(math.log2(n)) + 1) - 1
        return mask ^ n