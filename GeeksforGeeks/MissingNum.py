#https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1/
class Solution:
    def MissingNumber(self,array,n):
        '''
        Just because every number is distinct, we can easily find the missing number in 
        the range [1,N]
        '''
        array = set(array)  #Asymptotic TC is O(N) because we have to iterate over all list items
        for i in range(1,n+1):
            if i not in array:
                return i