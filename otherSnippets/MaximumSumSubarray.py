arr = [4,-11,1,6,2,3,-2]
# arr = [2,9,5]
s = 0

pf = [0]*len(arr)
pf[0] = arr[0]
for i in range(1,len(arr)):
    pf[i] = pf[i-1] + arr[i]
for i in range(len(arr)):
    s = s + pf[i]
    for j in range(i+1,len(arr)):
        s += pf[j] - pf[i]
print('Sum of all subarrays:',s)


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
