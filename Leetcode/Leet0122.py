# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        
        max_profit = 0
        stock = arr[0]
        
        for i in range(1,len(arr)):
            diff = arr[i] - stock
            
            if diff > 0:
                # Need to find maximum possible profit
                max_profit += diff
                
                # After making profit we are assuming the buying price is current price
                stock = arr[i]
            elif diff < 0:
                stock = arr[i]
            
        return max_profit