class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if j!= i and nums[j] < nums[i]:
                    count += 1
            arr.append(count)
        return arr