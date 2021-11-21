# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
    
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = []
        for index,value in enumerate(nums):
            if value == target:
                l.append(index)
        if len(l) == 1: return l*2
        elif len(l) > 1: return [l[0],l[-1]]
        else: return [-1,-1]

#this is not a binary search(O(logn)) approach as in Java solution
#binary search implementation is remaining in this solution 