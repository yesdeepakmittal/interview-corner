class Solution:
    def search(self,arr,target):
        idx = self.interpolation_search(arr,target)
        return idx
    
    def interpolation_search(self,arr,target):
        start = 0
        end = len(arr) - 1
        
        x = target
        lo = start
        hi = end
        

        while lo <= hi:
            mid = lo + int((x - arr[lo])*(hi - lo)/(arr[hi] - arr[lo]))
            if mid > (len(arr) - 1):
                return -1
            if arr[mid] > target:
                hi = mid - 1
            elif arr[mid] < target:
                lo = mid + 1
            else:
                return mid
        return -1

arr = [1,2,3,4,5,6,11,31,33,34,45]
target = -1
print(Solution().search(arr,target))
