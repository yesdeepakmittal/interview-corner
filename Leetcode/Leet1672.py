#https://leetcode.com/problems/richest-customer-wealth/
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maX = 0
        for i in accounts:
            if sum(i) > maX:
                maX = sum(i)
        return maX
        