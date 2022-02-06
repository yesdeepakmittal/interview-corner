'''
A -> read only array of n integers
check if any ele occurs more than n/3 times|TC - O(N),linear time|SC - O(1),constant additional space


Max > n/3 elements -> 2
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        ele1 = 1  #random number
        ele2 = 2  #random number
        freq1 = 0
        freq2 = 0
        for i in A:
            if i == ele1:
                freq1 += 1
            elif i == ele2:
                freq2 += 1
            elif freq1 == 0:
                ele1 = i 
                freq1 = 1
            elif freq2 == 0:
                ele2 = i 
                freq2 = 1 
            
            # Current ele does not match to any of these two eles so reduce both
            else:
                freq1 -= 1
                freq2 -= 1
        
        freq1 = freq2 = 0
        for i in A:
            if i == ele1:
                freq1 += 1
            elif i == ele2:
                freq2 += 1
        
        if freq1 > len(A)/3:
            return ele1
        elif freq2 > len(A)/3:
            return ele2
        else:
            return -1