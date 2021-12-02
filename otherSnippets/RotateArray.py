'''
input - arr = [1,2,3,4,5,6,7]
        k = 3
ouput - [5,6,7,1,2,3,4]

method1 - TC - O(N) | SC - O(1)
'''

def method1(arr,k):
    '''
    This is in-place algorithm and SC - O(1)
    It will cause permanent change to the input array
    '''
    for i in range(k%len(arr)):
        arr.insert(0,arr[-1])
        del arr[-1]
    return arr

def method2(arr,k):
    return arr[len(arr) - k:] + arr[:len(arr) - k]

def method3(arr,k):
    return list(reversed(list(reversed(arr[:len(arr)-k]))+list(reversed(arr[len(arr)-k:]))))

def method3_ext(arr,k):  #in-place method SC - O(1) | TC - O(N)
    def rev(arr):
        start = 0
        end = len(arr) - 1
        while start <= end:
            arr[start],arr[end] = arr[end],arr[start] 
            start += 1
            end   -= 1
        return arr 

    return rev(rev(arr[:len(arr)-k]) + rev(arr[len(arr)-k:]))

arr = [1,2,3,4,5,6,7,8]
print("Result of method1: ",end="")
print(method1(arr,3))

arr = [1,2,3,4,5,6,7,8]
print("Result of method2: ",end="")
print(method2(arr,3))

arr = [1,2,3,4,5,6,7,8]
print("Result of method3: ",end="")
print(method3(arr,3))

arr = [1,2,3,4,5,6,7,8]
print("Result of method3_ext: ",end="")
print(method3_ext(arr,3))
