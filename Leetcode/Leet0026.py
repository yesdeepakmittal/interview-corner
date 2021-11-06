#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums = sorted(list(set(nums)))
        index = 0
        while index < len(nums)-1: 
            if nums[index] == nums[index+1]: 
                nums.pop(index)
            else:
                index += 1
        return len(nums)
        