def removeDuplicates(arr,n):
    # Write your code here.
    index = 0
    cnt = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[index]:

            arr[index + 1] = arr[i]
            
            index += 1
            cnt += 1

    return cnt

if __name__ == '__main__':
    arr = [1, 2, 2, 3, 3]
    print(removeDuplicates(arr, len(arr)))