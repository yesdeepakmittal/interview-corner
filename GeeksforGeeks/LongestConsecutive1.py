#https://practice.geeksforgeeks.org/problems/longest-consecutive-1s-1587115620/1/
class Solution:
    ##Complete this function
    # Function to calculate the longest consecutive ones
    def maxConsecutiveOnes(self, N):
        ##Your code here
        ans = 0
        cnt = 0
        num = bin(N)[2:]
        for i in num:
            if i == '1':
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans
