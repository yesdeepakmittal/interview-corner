#https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        mx = 0
        for key,value in d.items():
            if value > mx:
                mx = value
                k = key
        return k