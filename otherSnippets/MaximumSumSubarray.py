arr = [4,-11,1,6,2,3,-2]
#Maximum sum subarray

'''
TC - O(N2) | SC - O(1)
'''
MaxSum = -11111111
for i in range(len(arr)):
    s = 0
    for j in range(i,len(arr)):
        s += arr[j]
        if s > MaxSum:
            MaxSum = s
print('MaxSum is ->',MaxSum)


'''
TC - O(N) | SC - O(1)
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, arr):
        import sys

        MaxSum = -sys.maxsize - 1

        # for i in range(len(arr)):
        #     s = 0
        #     for j in range(i,len(arr)):
        #         s += arr[j]
        #         if s > MaxSum:
        #             MaxSum = s
        # return MaxSum
        
        #Kadane Algo
        max_end_here = 0
        for i in arr:
            max_end_here += i
            if MaxSum < max_end_here:
                MaxSum = max_end_here

            if max_end_here < 0:
                max_end_here = 0
        return MaxSum 
