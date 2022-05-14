#https://practice.geeksforgeeks.org/problems/find-first-set-bit-1587115620/1/
class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        #Your code here
        first_set_bit = n & -n
        # n = bin(first_set_bit)[2:][::-1]
        # try:
        #     idx = n.index('1') + 1
        # except ValueError:
        #     idx = 0
        
        # return  idx
        
        'TC - O(logN) | SC - O(1)'
        
        if first_set_bit == 0:
            return 0
        
        import math
        return int(math.log2(first_set_bit)) + 1