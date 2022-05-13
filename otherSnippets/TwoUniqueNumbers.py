'''
Find the two numbers that are unique in the array. 
TC - O(N) | SC - O(1)
'''


class Solution:
    def singleNumber(self, nums):
        xor = 0
        for i in range(len(nums)):
            xor = xor ^ nums[i]
        
        #finding first set bit in xor
        # first_set_bit = xor & -xor # 2's complement method to find first set bit
        first_set_bit = xor & ~(xor - 1)
        
        sum1 = 0
        sum2 = 0
        for i in range(len(nums)):
            if (nums[i] & first_set_bit):
                sum1 = sum1 ^ nums[i]
            else:
                sum2 = sum2 ^ nums[i]
        return sorted([sum1,sum2])

print(Solution().singleNumber([1,2,3,2,1,4]))