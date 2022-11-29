#https://practice.geeksforgeeks.org/problems/plus-one/1

class Solution:
    def increment(self, arr, N):
        # code here 
        
        carry = 1
        
        for i in range(len(arr)- 1, -1, -1):
            mod = (arr[i] + carry) % 10
            
            if (mod == 0) and (arr[i] != 0):
                arr[i] = 0
                carry = 1
            else:
                arr[i] = arr[i] + carry
                carry = 0
        
        if carry == 1:
            arr.insert(0,1)
        return arr