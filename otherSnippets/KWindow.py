'''
Find the number of distinct elements in a window size of K
How many windows can be there? N - K + 1
'''

# TC - O(kN) | O(k)
A = [6,3,7,3,8,6,9]
k = 3
ans = []
for i in range(len(A) - k + 1):
    d = {}
    for j in range(i,i+k):
        if A[j] in d:
            d[A[j]] += 1
        else:
            d[A[j]] = 1
    ans.append(len(d))
print(ans)


#TC - 
ans = []
d = {}
for i in range(k):
    if A[i] in d:
        d[A[i]] += 1
    else:
        d[A[i]] = 1
ans.append(len(d))
for i in range(k,len(A)):
    d[A[i-k]] -= 1
    if d[A[i-k]] == 0:
        del d[A[i-k]]
    if A[i] in d:
        d[A[i]] += 1
    else:
        d[A[i]] = 1
    ans.append(len(d))
print(ans)