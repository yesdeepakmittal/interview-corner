#https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            i = nums.index(target)
        except:
            i = -1
        return i
        