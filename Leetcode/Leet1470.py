class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = nums.copy()
        j = 0
        for i in range(n):
            arr[j] = nums[i]
            j += 1
            arr[j] = nums[i+n]
            j += 1
        return arr