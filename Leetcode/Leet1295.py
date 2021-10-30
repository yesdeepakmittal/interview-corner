# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         count = 0
#         for i in nums:
#             if len(str(i))%2 == 0:
#                 count = count + 1
#         return count



nums = [12,345,2,6,7896] 
def findNumbers(nums:list) -> int:
    count = 0
    for i in nums:
        if len(str(i))%2 == 0:
            count = count + 1
    return count
print(findNumbers(nums))