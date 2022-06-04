#https://practice.geeksforgeeks.org/problems/square-root/1/
class Solution:
    def floorSqrt(self, x): 
        start = 0
        end = x
        
        while start <= end:
            mid = (start + end) >> 1
            
            if mid*mid > x:
                end = mid - 1
            elif mid*mid < x:
                start = mid + 1
            else:
                return int(mid)
        return int(end)