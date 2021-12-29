# no. of subarray of length K = n-k+1

arr = [1,2,3,4,5]
n = len(arr)
k = 3
for i in range(0,n-k+1):
    j = i + k -1
    print(i,j)

