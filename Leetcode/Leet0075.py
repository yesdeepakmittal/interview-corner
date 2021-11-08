nums = [2,0,2,1,1,0]
if len(nums) == 1:
    nums
elif len(nums) == 2:
    if nums[0] > nums[1]:
        nums[0],nums[1] = nums[1],nums[0]
else:
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
print(nums)