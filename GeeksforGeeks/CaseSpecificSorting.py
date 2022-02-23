#https://practice.geeksforgeeks.org/problems/case-specific-sorting-of-strings4845/1/

class Solution:
    def caseSort(self,s):
        lower = ''
        upper = ''
        for i in s:
            if i.lower() == i:
                print(i)
                lower = lower + i
            else:
                upper += i
        lower = sorted(lower)
        upper = sorted(upper)
        # print(lower)
        # print(upper)
        ans = ''
        a = 0
        b = 0
        for i in s:
            if i.lower() == i:
                ans += lower[a]
                a += 1
            else:
                ans += upper[b]
                b += 1
        return ans

print(Solution().caseSort('defRTSersUXI'))