#https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0,  x
        while start <= end:
            mid = start + (end - start) // 2

            if mid * mid > x:
                end = mid - 1
            elif mid * mid < x:
                start = mid + 1
            else:
                return mid

        return end
        