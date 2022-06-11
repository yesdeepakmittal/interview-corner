#https://practice.geeksforgeeks.org/problems/missing-number4257/1/

def missingNumber( A, N):
     """
     Sorting is not allowed
     We can not use extra space-otherwise we could convert list -> set 
        and find the missing number while iterating and checking the number in the set
     
     Since the number is starting from the 1 till N simply find the sum of N natural number 
        and then sum of array then find d/fce
     """
     
     # sum of n natural number
     s = N*(N + 1)//2
     return s - sum(A)