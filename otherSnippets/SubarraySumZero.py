''''
Check Whether their is any subarray whose sum is zero in the array

Brute Force - O(N3)
Optimized - O(N) | SC - O(1)
'''

def check_bf():
    arr = [2,2,1,-3,4,3,1,-2,-3]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            s = sum(arr[i:j+1])  # O(N) complexity

            if s == 0:
                return True
    return False

def opt():
    arr = [2,2,1,-3,4,3,1,-2,-3]

    pf = [0]*(len(arr)+1)

    for i in range(len(arr)):
        pf[i+1] = pf[i] + arr[i]
    
    d = {}
    for i in pf:
        if i in d:
            return True
        else:
            d[i] = 1
    return False