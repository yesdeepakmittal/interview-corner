#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers) - 1
        while a < b:
            if numbers[a] + numbers[b] < target: a = a + 1
            elif numbers[a] + numbers[b] > target: b = b - 1
            else: return [a + 1, b + 1]