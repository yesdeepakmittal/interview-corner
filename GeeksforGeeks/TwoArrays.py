#https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1/
class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        d1 = {}
        d2 = {}
        for i in range(N):
            if A[i] in d1:
                d1[A[i]] += 1
            else:
                d1[A[i]] = 1
            
            if B[i] in d2:
                d2[B[i]] += 1
            else:
                d2[B[i]] = 1
        return d1 == d2