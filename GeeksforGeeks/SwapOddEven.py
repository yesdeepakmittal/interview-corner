#https://practice.geeksforgeeks.org/problems/swap-all-odd-and-even-bits-1587115621/1/
class Solution:
    
    ##Complete this function
    #Function to swap odd and even bits.
    def swapBits(self,n):
        #Your code here
        # 00010111
        # 00101011
        ans = ''
        num = bin(n)[2:]
        if len(num)%2 != 0:
            num = '0' + num
        for i in range(0,len(num),2):
        	ans += num[i+1] 
        	ans += num[i] 
        return int(ans,base=2)