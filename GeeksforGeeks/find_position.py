#https://practice.geeksforgeeks.org/problems/find-position-of-set-bit3706/1/

class Solution:
    def findPosition(self, N):
        # code here 
        cnt = 0
        temp = N
        while temp>0:
            temp = temp&(temp-1)  #counting the set bits
            cnt +=1 
        if cnt == 0 or cnt >1:
            return -1
        
        #finding the position of first set bit using the 2's complement
        first_set_bit = N & -N
        import math
        return int(math.log2(first_set_bit)) + 1