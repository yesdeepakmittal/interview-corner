#https://practice.geeksforgeeks.org/problems/1s-complement2819/1/
class Solution:
    def onesComplement(self,S,N):
        # code here
        ans = ''
        for i in S:
            if i == '1':
                ans += '0'
            else:
                ans += '1'
        return ans