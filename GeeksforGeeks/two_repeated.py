#https://practice.geeksforgeeks.org/problems/two-repeated-elements-1587115621/1

class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , N):
        #Your code here
        
        s = set()
        
        ans = [0,0]
        idx = 0
        
        for i in range(len(arr)):
            if arr[i] in s:
                ans[idx] = arr[i]
                idx += 1
            else:
                s.add(arr[i])
        
        return ans
