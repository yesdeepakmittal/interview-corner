https://leetcode.com/problems/remove-element/
    
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = list(filter(lambda var:var != val, nums))
        l = len(nums)
        return l
