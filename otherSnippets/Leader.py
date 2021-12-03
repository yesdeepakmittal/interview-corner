arr = [-7,1,5,2,-4,3,0]

leader = arr[-1]
count = 1

for i in range(len(arr)-2,-1,-1):
    if arr[i] > leader:
        count += 1
        leader = arr[i]

print(count)