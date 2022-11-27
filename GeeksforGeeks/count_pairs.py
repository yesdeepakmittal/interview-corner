# https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        d = {}
        cnt = 0
        for i in range(len(arr)):
            if arr[i] in d:
                cnt += d[arr[i]]
            
            d[k - arr[i]] = d.get(k - arr[i],0) + 1
        
        return cnt