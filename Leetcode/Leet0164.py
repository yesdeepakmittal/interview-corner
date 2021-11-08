#https://leetcode.com/problems/maximum-gap/
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        else:
            nums.sort()
            arr = []
            for i in range(len(nums)-1):
                arr.append(nums[i+1] - nums[i])
        return max(arr)
        