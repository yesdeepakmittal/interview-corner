size = int(input())
for i in range(size):
    N,K,M = map(int,input().split())
    arr = list(map(int,input().split()))
    ans = []
    
    #no. of subarrays of size K -> (N - K + 1)
    # j = i + K - 1
    
    for i in range(N - K + 1):
        j = i + K - 1
        s = sum(arr[i:j+1])
        ans.append(s)
    
    ans.sort()
    for i in reversed(ans[-M:]):
        print(i,end=' ')
    print()