#https://practice.geeksforgeeks.org/problems/peak-element/1#
class Solution:   
    def peakElement(self,nums, n):
        # Code here
        start = 0
        end = n-1
        while start < end:
            mid = start + (end-start)//2
            if nums[mid] > nums[mid+1]:
                #you are in decreasing part
                end = mid
            else:
                #you are in increasing part
                start = mid+1
        return start #or end as both are equal