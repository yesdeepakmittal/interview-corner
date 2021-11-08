https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in digits:
            s += str(i)
        arr = []
        for i in str(int(s) + 1):
            arr.append(int(i))
        return arr
        
