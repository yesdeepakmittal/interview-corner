#https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1

class Solution:
    def pushZerosToEnd(self,arr):
        '''
         - TC - O(N)
         - SC - O(1)
        '''
        
        zero_idx = 0
        
        for i in range(len(arr)):
            if arr[i] != 0:
                
                '''
                 - value of zero_idx and i will be same till they will get non-zero values
                 - if it will find zero value, i keep incrementing but zero_idx will not
                '''
                
                arr[zero_idx] = arr[i]
                zero_idx += 1
        
        for remaining_zero_idx in range(zero_idx,len(arr)):
            arr[remaining_zero_idx] = 0
        
        return arr

print(Solution().pushZerosToEnd([3, 5, 0, 0, 4]))