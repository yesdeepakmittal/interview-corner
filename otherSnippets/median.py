'''
TC - O(NlogN)
'''

def median(arr,N):
    arr.sort()

    if N % 2 == 0:
        median = (arr[N//2 - 1] + arr[N//2])/2
    else:
        median = arr[N//2]   # or arr[(N-1)//2]
