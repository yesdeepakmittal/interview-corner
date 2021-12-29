#sum of all subarray
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