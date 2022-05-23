#https://practice.geeksforgeeks.org/problems/check-set-bits5408/1/
class Solution:
    def isBitSet (self, N):
        # code here 
        if N == 0:
            return 0
        import math
        length = int(math.log2(N)) + 1
        
        cnt = 0
        while N > 0:
            N = N & (N - 1)
            cnt += 1
        if cnt == length:
            return 1
        return 0