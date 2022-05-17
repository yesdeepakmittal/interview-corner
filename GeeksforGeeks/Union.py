#https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1/

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        #code here
        ans = set()
        for i in a:
            ans.add(i)
        for i in b:
            ans.add(i)
        return len(ans)