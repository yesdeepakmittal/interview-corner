#https://practice.geeksforgeeks.org/problems/reverse-bits3556/1/
class Solution:
    def reversedBits(self, X):
        # code here 
        num = bin(X)[2:]
        diff = 32 - len(num)
        num = '0'*diff + num
        num = num[::-1]
        return int(num,base=2)