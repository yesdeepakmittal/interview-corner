#https://practice.geeksforgeeks.org/problems/find-out-the-team0025/1/
class Solution:
    def half(self, N):
        # code here
        if N == 1: return N
        return N >> 1