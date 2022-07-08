'''TC - Log3N'''
def ternarySearch(arr,target):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        mid1 = start + (end - start)//3
        mid2 = mid1 + (end - start)//3
        
        if arr[mid1] == target:
            return mid1
        
        elif arr[mid2] == target:
            return mid2
        
        elif arr[mid1] > target:
            end = mid1 - 1
        
        elif arr[mid2] < target:
            start = mid2 + 1
    return -1
    
arr = [1,2,3,4,5,6]
target = 5

print(ternarySearch(arr,target))
