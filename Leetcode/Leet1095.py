#https://leetcode.com/problems/find-in-mountain-array/
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        peak = self.PeakIndexInMountainArray(arr)
        firstHalf = self.OrderAgnosticBS(arr,target,0,peak)
        if firstHalf != -1:
            return firstHalf
        return self.OrderAgnosticBS(arr,target,peak+1,arr.length() - 1)
        
    def PeakIndexInMountainArray(self,arr):
        start = 0
        end = arr.length() - 1
        while start < end:
            mid = start + (end - start)//2          #equivalent of (start + end) >> 1  
            if arr.get(mid) > arr.get(mid + 1):
                end = mid
            else:
                start = mid + 1
        return start
    
    def OrderAgnosticBS(self,arr,target,start,end):
        tempBool = arr.get(start) < arr.get(end)
        while start <= end:
            mid = start + (end - start)//2
            if arr.get(mid) == target:
                return mid
            
            if tempBool:
                if target > arr.get(mid):
                    start = mid + 1
                elif target < arr.get(mid):
                    end = mid - 1
                else:
                    return mid
            else:
                if target < arr.get(mid):
                    start = mid + 1
                elif target > arr.get(mid):
                    end = mid - 1
                else:
                    return mid
        return -1
        