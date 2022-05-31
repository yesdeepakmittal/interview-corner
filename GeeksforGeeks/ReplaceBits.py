#https://practice.geeksforgeeks.org/problems/replace-the-bit3212/1/

class Solution:
    def replaceBit(self, N, K):
        '''
        maximum number in 3 bits -> 7(111) not 8 so log2(7) != 3, it is 2, so +1
        log2(n) + 1
        Just because we have to change the bit from left side, if K > length of binary number, return the number itself.
        
        '''
        
        import math
        limit = int(math.log2(N)) + 1
        if K > limit: #if K > length(N) in binary [LEFT SIDE]
            return N
            
        n = 1 << (limit-K)  #finding the bit position
        n = ~n  #taking the complement to invert other bits to 1 and required bit to 0
        return n & N