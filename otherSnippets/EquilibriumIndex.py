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

after = [0]*len(arr)
before = [0]*len(arr)

for i in range(1,len(arr)):
    before[i] = before[i-1] + arr[i-1]

for i in range(len(arr) - 2, -1, -1):
    after[i] = after[i+1] + arr[i+1]

for i in range(len(arr)):
    if before[i] == after[i]:
        print(i)