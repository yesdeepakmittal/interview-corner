# https://www.codingninjas.com/studio/problems/ninja-and-the-sorted-check_6581957

def isSorted(n: int,  arr: [int]) -> int:
    # Write your code here.

    # if len(arr) == 1:
    #     return 1

    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return 0
    
    return 1


if __name__ == '__main__':
    arr = [1,2,3,4,5,6]

    print(isSorted(len(arr), arr))