#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # arr = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        # TC - O(N) | SC - O(N) | Hashing 
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]],i]
            else:
                d[target - nums[i]] = i
        return []