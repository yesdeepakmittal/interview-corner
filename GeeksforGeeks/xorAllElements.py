#https://practice.geeksforgeeks.org/problems/xor-of-all-elements0736/1/
class Solution:
    def getXor(self, A, N):
        # code here
        xor = 0
        for i in A:
            xor = xor ^  i
        
        for i in range(N):
            A[i] = xor ^ A[i]
        
        return A