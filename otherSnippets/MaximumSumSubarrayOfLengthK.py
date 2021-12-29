# arr = [4,-11,1,6,2,3,-2]
arr = [1,2,3,4,5]
# arr = [2,9,5]
k = 3
pf = [0]*len(arr)
pf[0] = arr[0]
for i in range(1,len(arr)):
    pf[i] = pf[i-1] + arr[i]

# number of subarry of length k is N-k+1
MaxSum = pf[k-1]
for i in range(k,len(arr)):
    if pf[i] - pf[i-k] > MaxSum:
        MaxSum = pf[i]  - pf[i-k]

print('MaxSum is ->',MaxSum)


#sliding window technique TC- O(N) | SC - O(1)
sm = sum(arr[:k])
MaxSum = sm
n = len(arr)
for i in range(k,n):
    sm = sm + arr[i]
    sm = sm - arr[i-k]
    if sm > MaxSum:
        MaxSum = sm
print(MaxSum)