#https://leetcode.com/problems/find-pivot-index/
#https://github.com/yesdeepakmittal/competitive-coding/blob/main/otherSnippets/EquilibriumIndex.py
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pf = [0]*n
        after_sum = [0]*n 
        before_sum = [0]*n
        
        
        pf[0] = nums[0]
        for i in range(1,n):
            pf[i] = pf[i-1] + nums[i]
        
        before_sum[0] = 0
        for i in range(1,n):
            before_sum[i] = pf[i-1]
        
        after_sum[-1] = 0
        for i in range(n-1):
            after_sum[i] = pf[n-1] - pf[i]
        
        for i in range(n):
            if before_sum[i] == after_sum[i]:
                return i
        return -1