# https://practice.geeksforgeeks.org/problems/maximum-repeating-number4858/1/
class Solution:

    def maxRepeating(self,arr, n, k):
        # code here
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        ans = k
        ans_value = 0
        for key in range(k-1,-1,-1):
            if key in d:
                if d[key] >= ans_value:
                    ans_value = d[key]
                    ans = key
        return ans