'''
- Applicable only if heights are positive
- length of array > 2
- Trapped water is positive - if current bar > min(max_left,max_right) then it will be -ve

TC - O(N) | SC - O(N)
'''

arr = [4,2,0,6,3,2,5]

left_max = [0]*len(arr)
right_max = [0]*len(arr)

# left_max[0] = arr[0]
# right_max[-1] = arr[-1]

for i in range(1,len(arr) - 1):
    left_max[i] = max(left_max[i-1],arr[i-1])

for i in range(len(arr) - 2, 0, -1):
    right_max[i] = max(right_max[i+1],arr[i+1])

total_water = 0
if len(arr) > 2:
    for i in range(1,len(arr) - 1):
        # max_left = max(arr[:i])
        # max_right = max(arr[i+1:])

        # water_level = min(max_left,max_right)
        water_level = min(left_max[i],right_max[i])

        trapped_water = water_level - arr[i]

        if trapped_water > 0:
            total_water += trapped_water

print(total_water)
        