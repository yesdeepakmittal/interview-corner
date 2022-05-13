class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        ##Your code here
        cnt = 0
        while n > 0:
            n = n&(n-1)
            cnt += 1
            
        if cnt == 1:
            return True
        return False