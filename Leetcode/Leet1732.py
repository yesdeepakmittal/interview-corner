class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = [0] + gain
        for i in range(len(gain)):
            arr[i+1] = arr[i] + gain[i]
        return max(arr)
        