""""
Number of elements strictly less than current number = current number
"""
#for distinct elements only
arr = [1,-5,3,5,-10,4]
arr.sort()
print(arr)
for i in range(len(arr)):
  if arr[i] == i:
    print(arr[i])

#for distinct & non-distinct elements
# arr = [-3,0,2,4,5,5,5,5,8,8,10,10,10]
arr.sort()
l = [0]

for i in range(1,len(arr)):
  if arr[i-1] == arr[i]:
    l.append(l[-1])
  else:
    l.append(i)
# print(l)
cnt = 0
for i in range(len(arr)):
  if arr[i] == l[i]: 
    cnt += 1
    print(arr[i])

print('Count:',cnt)