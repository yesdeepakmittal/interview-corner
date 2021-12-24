arr = [9,14,21,7,-3,4,26,10]
arr.sort()
import sys
mn = sys.maxsize

for i in range(len(arr)-1):
  temp = abs(arr[i] - arr[i+1])
  if temp < mn:
    mn = temp
print(mn)