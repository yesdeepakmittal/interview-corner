"""
input arr = [1,2,3,4,5,6,7,8]
output arr = [8,7,6,5,4,3,2,1]
Method 1 = TC - O(N) | SC - O(N)
method 2 = TC - O(N) | SC - (1) - No extra space used
method 3 = TC - O(N) | SC - (?)
method 4 = TC - O(N) | SC - (?)
method 5 = TC - O(N) | SC - (?)
"""

def method1(arr):
    arr2 = []
    for i in range(len(arr)-1,-1,-1):
        arr2.append(arr[i])
    return arr2

def method2(arr):
    '''
    This method performs in-place operation
    It will cause permanent change to input array
    Also work for Tuple and when we need to reverse a part of an Array(just add start & end value)
    '''
    start = 0
    end = len(arr) - 1
    while start <= end:
        arr[start],arr[end] = arr[end],arr[start] 
        start += 1
        end   -= 1
    return arr 

def method3(arr):
    '''
    This method uses slicing Operator
    '''
    return arr[::-1]

def method4(arr):
    '''
    This method uses mutator method of class list
    It will cause permanent change to the input array
    '''
    arr.reverse()
    return arr

def method5(arr):
    '''
    This method uses in-built reversed() fn
    '''
    return list(reversed(arr))

arr = [1,2,3,4,5,6,7,8]
print("Result of method1: ",end="")
print(method1(arr))

arr = [1,2,3,4,5,6,7,8]
print("Result of method2: ",end="")
print(method2(arr))

arr = [1,2,3,4,5,6,7,8]
print("Result of method3: ",end="")
print(method3(arr))

arr = [1,2,3,4,5,6,7,8]
print("Result of method4: ",end="")
print(method4(arr))

arr = [1,2,3,4,5,6,7,8]
print("Result of method5: ",end="")
print(method5(arr))


'''
Output

Result of method1: [8, 7, 6, 5, 4, 3, 2, 1]
Result of method2: [8, 7, 6, 5, 4, 3, 2, 1]
Result of method3: [8, 7, 6, 5, 4, 3, 2, 1]
Result of method4: [8, 7, 6, 5, 4, 3, 2, 1]
Result of method5: [8, 7, 6, 5, 4, 3, 2, 1]
'''