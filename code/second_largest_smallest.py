def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    return approach2(n, a)


def approach1(n, arr):
    """
        TC - O(N)    | but there are 3 traversals, can we optimize it?
        SC - O(1)
    """
    largest = max(arr)
    smallest = min(arr)

    second_largest = float("-inf")
    second_smallest = float("inf")

    for i in range(n):
        if arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]

        if arr[i] < second_smallest and arr[i] != smallest:
            second_smallest = arr[i]
    
    return [second_largest, second_smallest]

def approach2(n, arr):
    """
        TC - O(N)   | Only one traversal
        SC - O(1)
    """
    largest = arr[0]
    smallest = arr[0]

    second_largest = float("-inf")
    second_smallest = float("inf")

    for i in range(n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]

        ## if we found the largest at index 0, then if will not execute, so update the second_largest otherwise
        elif arr[i] < largest:   # if arr[i] == largest, can't update it in second_largest
            if arr[i] > second_largest:
                second_largest = arr[i]

        
        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]
        
        elif arr[i] > smallest:
            if arr[i] < second_smallest:
                second_smallest = arr[i]

    return [second_largest, second_smallest]



if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]

    print(getSecondOrderElements(len(arr), arr))

    """
        [Handle edge case]
        If the value of second_smallest == float('inf') OR second_largest == float("-inf"):
            return -1
    """