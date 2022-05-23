#https://practice.geeksforgeeks.org/problems/rotate-bits4524/1/
class Solution:
    def rotate(self, N, D):
        D = D%16
        binary = bin(N)[2:]
        cnt = 16 - len(binary)
        N = '0'*cnt + binary
        left_rotate = N[D:] + N[:D]
        right_rotate = N[-D:] + N[:-D]
        return [int(left_rotate,base=2),int(right_rotate,base=2)]