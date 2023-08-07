# https://www.codingninjas.com/studio/problems/ninja-and-the-zero-s_6581958

def moveZeros(n: int,  arr: [int]) -> [int]:
    # Write your code here.

    zero_ptr = -1

    for i in range(len(arr)):
        
        # non-zero value
        if arr[i] != 0:
            if zero_ptr != -1 and zero_ptr < i:
                arr[i], arr[zero_ptr] = arr[zero_ptr], arr[i]
                zero_ptr += 1
        
        # zero value case
        else:
            if zero_ptr == -1:
                zero_ptr = i    

    return arr

if __name__ == "__main__":
    arr = [1, 2, 0, 0, 2, 3]   # best test case which helped me accurately design the logic

    print(moveZeros(len(arr), arr))