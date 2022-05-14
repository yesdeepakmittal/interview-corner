#https://practice.geeksforgeeks.org/problems/rightmost-different-bit-1587115621/1/
class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        #Your code here
        if m == n:
            return -1
        difference = m ^ n
        
        #finding the first set bit from left using the 2's complement
        first_set_bit = difference & -difference
        import math
        return int(math.log2(first_set_bit)) + 1