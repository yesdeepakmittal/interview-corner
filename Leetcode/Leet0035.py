#https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            idx = 0
            for i in nums:
                if i > target:
                    return idx
                else:
                    idx += 1
            return idx