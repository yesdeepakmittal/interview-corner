class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = ''
        for i in num:
            s += str(i)
        l = []
        var = int(s) + k
        for i in str(var):
            l.append(int(i))
        return l