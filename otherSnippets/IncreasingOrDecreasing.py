# [0,1,2,3,4]           return 1
# [0,5,7]               return 1
# [0,7,5]               return 0
# [7,5,0]               return 1


def fn(arr):
    if arr[0] <= arr[len(arr) - 1]:
        # array is increasing order

        for i in range(1,len(arr)):
            if arr[i] >= arr[i- 1]:
                continue
            else:
                return 0
        return 1
    else:
        for i in range(1,len(arr)):
            if arr[i] <= arr[i- 1]:
                continue
            else:
                return 0
        return 1
    
print(fn([0,1,2,3,2]))


'''
TC - O(N)
SC - O(1)
'''
def fn2(arr):
    increasing_order = 0
    decreasing_order = 0

    for i in range(1,len(arr)):
        if arr[i] > arr[i - 1]:
            increasing_order += 1
        elif arr[i] < arr[i - 1]:
            decreasing_order += 1

    if (increasing_order == 0 or decreasing_order == 0):
        return 1
    else:
        return 0
    
print(fn2([1,1,2,2,3]))