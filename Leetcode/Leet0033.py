#https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        # try:
        #     i = nums.index(target)
        # except:
        #     i = -1
        # return i
        
        pivot = self.FindPivot(arr)
        if pivot == -1:
            return self.binarySearch(arr,target,0,len(arr)-1)
        if arr[pivot] == target:
            return pivot
        if arr[0] <= target:
            return self.binarySearch(arr,target,0,pivot-1)
        else:
            return self.binarySearch(arr,target,pivot+1,len(arr)-1)
    
    def FindPivot(self,arr):
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = start + (end - start)//2
            if mid < end and arr[mid] > arr[mid + 1]:
                return mid
            elif start < mid and arr[mid] < arr[mid - 1]:
                return mid - 1
            elif arr[start] >= arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    
    def binarySearch(self,arr,target,start,end):
        while start <= end:
            mid = start + (end - start)//2
            if arr[mid] > target:
                end = mid - 1
            elif arr[mid] < target:
                start = mid + 1
            else:
                return mid
        return -1
