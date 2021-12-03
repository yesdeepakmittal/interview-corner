arr = [-3,6,2,4,5,2,8,-9,3,1]

#Brute Force
# TC - O(Q*N) | SC - O(1)
# Answering any query in q time and calculating sum in N time
# if q ~ N, TC - O(N2)
query = [[1,5],[4,7]]
for i in query:
    s = 0
    for j in range(i[0],i[1]+1):
        s += arr[j]
    print(s)
# To answer a single query, it takes N time - 1*N

#Prefix-sum - Need to maintain cumulative sum
# TC - O(N) | SC - O(N)
pf = [0]*len(arr)
pf[0] = arr[0]
for i in range(1,len(arr)):
    pf[i] = pf[i-1] + arr[i]

for i in query:
    print(pf[i[1]] - pf[i[0] - 1])

#To answer a single query, it takes constant time
print(pf[5]-pf[2])



runs = {1:2, 2:8, 3: 14, 4:29, 5:31, 6:49, 7:65, 8:79,9:88,10:97}
#score made in over[2-3]
# runs[i,j] = runs[j] - runs[i-1]
print(runs[3] - runs[1])


#Optimizing space of Prefix-sum
# TC - O(N) | SC - O(1) - Best case
arr = [-3,6,2,4,5,2,8,-9,3,1]

for i in range(1,len(arr)):
    arr[i] = arr[i-1] + arr[i]
for i in query:
    print(arr[i[1]] - arr[i[0] - 1])


'''
for 1-indexed
arr = [1, 2, 3, 4, 5]
query = [[1, 4], [2, 3]]
output = [10, 5]
'''

def rangeSum(self, A, B):
    ans = []
    pf = [0]*(len(A)+1)
    for i in range(1,len(A)+1):
        pf[i] = pf[i-1] + A[i-1]
    for i in B:
        ans.append(pf[i[1]] - pf[i[0]-1])
    return ans