#sum of all subarray

'TC - O(N2) | SC - O(N) even after using pf'
arr = [1,2,3,4,5]
pf = [0]*(len(arr)+1)
for i in range(len(arr)):
  pf[i+1] = pf[i] + arr[i]
print(pf)

sm = 0
for i in range(len(arr)):
  for j in range(i+1,len(arr)+1):
    sm += pf[j] - pf[i]
print(sm)


'TC - O(N) | SC - O(1) - super'
sm = 0
n = len(arr)
for i in range(n):
    start_index = i + 1
    end_index   = n - i
    sm += arr[i]*(start_index*end_index)
print(sm)