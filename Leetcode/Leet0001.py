class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,v in enumerate(nums):
            if v in d:
                return [d[v], i]
            else:
                d[target - v] = i