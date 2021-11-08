class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = matrix[0]
        for i in matrix[1:]:
            arr += i
        
        #best case
        if arr[0] == target or arr[-1] == target:
            return True
        
        #Let's do binary search
        start = 0
        end = len(arr) - 1
        
        while(start <= end):
            mid = start + (end - start)//2
        
            if target < arr[mid]:
                end = mid -1
            elif target > arr[mid]:
                start = mid + 1
            else:
                return True
        return False