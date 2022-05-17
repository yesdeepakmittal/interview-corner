#https://practice.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1/?
class Solution:
    #Complete the below function
    def search(self,arr, N, X):
        #Your code here
        try:
            ans = arr.index(X)
        except ValueError:
            ans = -1
        return ans