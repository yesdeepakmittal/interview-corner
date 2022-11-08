'''
Brute Force
TC - O(k2)  | SC - O(K)

if k ~ N, TC = O(N2)
'''

arr = [5,-2,3,1,2]
k = 3
s = []
for i in range(k):
    s.append(sum(arr[:i] + arr[-k+i:]))
print(max(s))


# TC - O(K2) | SC - O(1)
import sys
# maxSize = sys.maxsize
# minSize = -sys.maxsize - 1  # Just to deal with negative value test cases
maxSum = -sys.maxsize - 1
for i in range(k):
    s = sum(arr[:i] + arr[-k+i:])
    if s > maxSum:
        maxSum = s
print(maxSum)


# Prefix Sum
# TC - O(K) | SC - O(K)
pf = [0]*len(arr)
sf = [0]*len(arr)

pf[0] = arr[0]
for i in range(1,len(arr)):
    pf[i] = pf[i-1] + arr[i]

sf[-1] = arr[-1]
for i in range(len(arr)-2,-1,-1):
    sf[i] = sf[i-len(arr)+1] + arr[i-len(arr)]
# print(sf)

maxSum = -sys.maxsize - 1
for i in range(k):
    s = 0
    if i == 0:
        s += 0
    else:
        s += pf[i-1]
    
    if i==k:
        s += 0
    else:
        s += sf[-k+i]
    
    if s > maxSum:
        maxSum = s
print(maxSum)


'''
Output

8
8
8
'''





class Solution:
    def solve(self, arr, k):
        pf = [0]*(len(arr) + 1)
        sf = [0]*(len(arr) + 1)
        maxSum = float('-inf')

        for i in range(len(arr)):
            pf[i+1] = pf[i] + arr[i]
        
        for i in range(len(arr) - 1, -1, -1):
            sf[i] = sf[i+1] + arr[i]
        
        for i in range(0,k+1):
            s = pf[i] + sf[-(k+1) + i]
        
            if s > maxSum:
                maxSum = s
        return maxSum