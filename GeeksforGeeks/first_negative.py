#https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1

def sol1(arr,N, K):
    '''
     - TC - O(N)
     - SC - O(N)
    '''
    arr2 = [0]*len(arr)
    
    for i in range(len(arr)):
        if arr[i] < 0:
            arr2[i] = arr[i]
            
    cnt = len(arr)
    
    for i in range(len(arr) - 1, -1, -1):
        if arr2[i] != 0:
            cnt = 1
            continue
        
        if cnt < K:
            arr2[i] = arr2[i+1]
            cnt += 1
    
    ans = [0]*(N - K + 1)
    
    for i in range(0, N - K + 1):
        ans[i] = arr2[i]
    return ans

def sol2(arr,N, K):
    '''
     - TC - O(N)
     - SC - O(1)
    '''
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = 0
            
    cnt = len(arr)
    
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != 0:
            cnt = 1
            continue
        
        if cnt < K:
            arr[i] = arr[i+1]
            cnt += 1
    
    return arr[:N - K + 1]



def printFirstNegativeInteger( arr, N, K):
    # code here
    return sol2(arr, N , K)