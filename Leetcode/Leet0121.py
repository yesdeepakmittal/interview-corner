# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        
        max_profit = 0
        stock = arr[0]
        
        for i in range(1,len(arr)):
            diff = arr[i] - stock
            
            if diff > 0:
                max_profit = max(max_profit, diff)
            elif diff < 0:
                stock = arr[i]
            
        return max_profit