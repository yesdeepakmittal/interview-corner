#https://practice.geeksforgeeks.org/problems/bit-difference-1587115620/1/
class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        ##Your code here
        '''Firstly calculate the XOR of both number
           - Number of set bits in the XOR indicates where bits of two numbers differs
           - Simply calculate the number of set bits and that's the answer
        '''
        res = a ^ b
        cnt = 0
        while res > 0:
            res = res & (res - 1)
            cnt += 1
        return cnt