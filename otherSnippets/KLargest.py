'''
Find Kth largest Number in an array

Freecodecamp - https://youtu.be/Peq4GCPNC5c
'''

def method1(arr,k):
    # TC - O(kN)
    for i in range(k-1):  # k - 1
        arr.remove(max(arr)) # N + N

    return max(arr)  # N

def method2(arr,k):
    # TC - O(NlogN)
    arr.sort()
    return arr[len(arr) - k]

def method3(arr,k):
    #TC - O(N + klogN)
    import heapq
    arr = [-elem for elem in arr]  #because Py implements max heap
    heapq.heapify(arr)
    for i in range(k - 1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)