''''
Given an array, find first and last index of target element in a sorted array

A = [2,4,5,5,5,5,5,6,7]
o/p = [2,6]
'''
A = [2,4,5,5,5,5,5,6,7]

def flsorted1(arr,target):
    #TC - O(N) | SC-O(1)
    for i in range(len(arr)):
        if arr[i] == target:
            temp = i
            while i+1 < len(arr) and arr[i+1] == target:
                i += 1
            return [temp,i]
    return [-1,-1]


def flsorted2(arr,target):
    def search(arr,target,firstIndex):
        start = 0
        end = len(arr) - 1
        ans = -1
        while start <= end:
            mid = start + (end - start)//2
            if target < arr[mid]:
                end = mid - 1
            elif target > arr[mid]:
                start = mid + 1
            else:
                ans = mid
                if firstIndex:
                    end = mid - 1
                else:
                    start = mid + 1
        return ans
    
    ans = [-1,-1]
    ans[0] = search(arr,target,True)
    if ans[0] != -1:
        ans[1] = search(arr,target,False)
    return ans
    
print(flsorted1(A,5))
print(flsorted2(A,5))