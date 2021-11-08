#https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums):# List[int]) -> List[List[int]]:
        arr = []
        from itertools import combinations
        for i in range(len(nums)+1):
            arr += list(combinations(nums,i))
        return arr

if __name__ == "__main__":
    print(Solution().subsets([1,2,3]))
        