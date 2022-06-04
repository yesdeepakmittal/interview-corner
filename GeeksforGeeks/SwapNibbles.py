#https://practice.geeksforgeeks.org/problems/swap-two-nibbles-in-a-byte0446/1/

class Solution:
    def swapNibbles (self, N):
        # code here 
        import math
        length = int(math.log2(N)) + 1
        diff = 8 - length
        
        n = bin(N)[2:]
        n = '0'*diff + n
        return int(n[4:] + n[:4],base=2)