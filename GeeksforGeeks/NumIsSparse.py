#https://practice.geeksforgeeks.org/problems/number-is-sparse-or-not-1587115620/1/
class Solution:
    
    #Function to check if the number is sparse or not.
    def isSparse(self,n):
        #Your code here 
        num = bin(n)[2:]
        prev = num[0]
        for i in num[1:]:
            if i == '1' and prev == '1':
                return 0
            prev = i
        return 1