
arr = [5,4,1,3,2]

def bubble_sort(array):
    # Bubble Sort | TC - O(N2)

    arr = array.copy()  # Deep Copy
    swaps = 0
    for turn in range(len(arr)):
        for j in range(len(arr) - 1 - turn):
            if arr[j] > arr[j+1]:
                swaps += 1
                arr[j],arr[j+1] = arr[j+1],arr[j]
        
        if swaps == 0:
            # Best case | TC-O(N)
            print('Array is already sorted!')
            return arr
        # print(arr)

    return arr

def selection_sort(array):
    # Only swaps are lesser, TC is still O(N2)
    
    arr = array.copy()  # Deep Copy
    
    for turn in range(len(arr) - 1):
        minimum_pos = turn

        # find the index of minimum element starting i + 1 till end of array
        for j in range(turn + 1, len(arr)):
            if arr[j] < arr[minimum_pos]:
                minimum_pos = j
        
        # Swap the minimum element with the current index i(turn)
        arr[turn],arr[minimum_pos] = arr[minimum_pos],arr[turn]
    
    return arr

def insertion_sort(array):
    arr = array.copy()

    for current in range(1,len(arr)):
        current_element = arr[current]
        prev_idx = current - 1

        # Shifting all the unsorted elements to the right
        while (prev_idx >= 0) and (arr[prev_idx] > current_element):
            arr[prev_idx + 1] = arr[prev_idx]
            prev_idx -= 1

        # Doing insertion now
        arr[prev_idx + 1]  = current_element

    return arr

def counting_sort(array):
    arr = array.copy()

    ans = [0]*(max(arr) + 1)

    for i in arr:
        ans[i] += 1

    idx = 0
    for i in range(len(ans)):
        while ans[i] > 0:
            arr[idx] = i
            ans[i] -= 1
            idx += 1
    
    return arr



ans = counting_sort(arr)
print(ans)