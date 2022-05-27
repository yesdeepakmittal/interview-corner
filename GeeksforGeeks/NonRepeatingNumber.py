#https://practice.geeksforgeeks.org/problems/finding-the-numbers0215/1#

class Solution:
    def singleNumber(self, nums):
        # Code here
        xor = 0
        'The resulting xor will only have the xor of two Non repeating numbers'
        for i in range(len(nums)):
            xor ^= nums[i]
        
        '''- If two NON REPEATING numbers are DISTINCT, then their XOR != 0
           - now find the first set bit in the XOR of two number(if bit is 1, this bit is d/f in both numbers)
           - seperate all the numbers that have this bit as set bit and this bit unset
        '''
        # first_set_bit = xor & -xor
        first_set_bit = xor & ~(xor - 1)
        
        same_bit = 0
        different_bit = 0
        
        for i in range(len(nums)):
            if first_set_bit & nums[i]:
                same_bit ^= nums[i]
            else:
                different_bit ^= nums[i]
        
        'Now two DISTINCT numbers are seperated'
        
        return sorted([same_bit, different_bit])