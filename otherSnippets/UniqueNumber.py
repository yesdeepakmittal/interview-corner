nums = [1,1,1,2,2,2,3,4,4,4,5,5,5]

d = {}
k = 3
for i in nums:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

import sys
for key,value in d.items():
    if value%k:
        print(key)
        sys.exit()