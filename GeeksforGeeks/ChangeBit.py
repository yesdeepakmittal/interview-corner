#https://practice.geeksforgeeks.org/problems/change-all-even-bits-in-a-number-to-03253/1/
class Solution:
    def convertEvenBitToZero (ob, n):
        # code here 
        import math 
        length = int(math.log2(n)) + 1
        mask = 0
        
        '''
        N = 30 (11110) need to & with 01010
        2 + 8 = 01010
        '''
        for i in range(1,length,2):
            mask += 2**i
            
        return n & mask