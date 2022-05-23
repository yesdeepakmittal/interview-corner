#https://leetcode.com/problems/counting-bits/
class Solution:
#     def countBits(self, n: int) -> List[int]:
#         ans = [0]*(n + 1)
#         for i in range(1,n + 1):
#             ans[i] = self.count(i)
#         return ans
        
#     def count(self,n):
#         cnt = 0
#         while n > 0:
#             n = n & (n - 1)
#             cnt += 1
#         return cnt

        def countBits(self, n: int) -> List[int]:
            ans = [0 for i in range(n + 1)]
            for number in range(n + 1):
                ans[number] = (number & 1) + ans[number >> 1]
            return ans
        