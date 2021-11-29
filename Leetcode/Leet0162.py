#https://leetcode.com/problems/find-peak-element/submissions/
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # return nums.index(max(nums)) this is O(N)
        
        # below is binary search solution i.e. O(logN)
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + (end-start)//2
            if nums[mid] > nums[mid+1]:
                #you are in decreasing part
                end = mid
            else:
                #you are in increasing part
                start = mid+1
        return start #or end as both are equal
        