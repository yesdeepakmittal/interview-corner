'''
Sum of all elements before index i = Sum of all elements after index i
https://leetcode.com/problems/find-pivot-index/
'''

arr = [-7,1,5,2,-4,3,0]

#Brute Force
# TC - O(N2) | SC - O(1)
for i in range(len(arr)):
    if sum(arr[:i]) == sum(arr[i+1:]):
        print(i)

#Prefix-Sum
# TC - O(N) | SC - O(N)
# Space complexity can be reduced to 2N from 3N by calculating pf into arr itself
pf = [0]*len(arr)
before_sum = [0]*len(arr)
after_sum = [0]*len(arr)

pf[0] = arr[0]
for i in range(1,len(arr)):
    pf[i] = pf[i-1] + arr[i]

before_sum[0] = 0
for i in range(1,len(arr)):
    before_sum[i] = pf[i-1]


after_sum[-1] = 0
#After sum for index 0 is range[1,6] which is pf[6] - pf[1 - 1]
for i in range(len(arr) - 1):
    after_sum[i] = pf[len(arr) - 1] - pf[i]

for i in range(len(arr)):
    if before_sum[i] == after_sum[i]:
        print(i)