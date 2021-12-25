''''
Arrange an array in a way such that it will form largest sum
Avoid adding numbers as integer to prevent from verrrrryy long integer

TC - O(NlogN) - sorting cmplxty
'''

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        # from itertools import permutations
        # import sys
        # mx = - sys.maxsize - 1
        # l = list(permutations(A))
        
        # for i in l:
        #     temp = int(''.join([str(x) for x in i]))
        #     if temp > mx:
        #         mx = temp
        # return str(mx)
        A = [str(i) for i in A]
        # for i in range(len(A)-1):
        #     for j in range(i+1,len(A)):
        #         if int(A[i] + A[j]) < int(A[j] + A[i]):
        #             A[i],A[j] = A[j],A[i]
        # ans = ''.join(A)
        # try:
        #     temp = 0
        #     while ans[0] == '0':
        #         ans = ans[1:]
        #         temp += 1
        # except IndexError:
        #     return '0'
        # return ans
        from functools import cmp_to_key
        def my_cmp(a,b):
            if int(a + b) > int(b + a):
                return -1
            if int(a + b) < int(b + a):
                return 1
            return 0
        A.sort(key=cmp_to_key(my_cmp))
        ans = ''.join(A)
        try:
            temp = 0
            while ans[0] == '0':
                ans = ans[1:]
                temp += 1
        except IndexError:
            return '0'
        return ans

A = [3, 30, 34, 5, 9]
print(Solution().largestNumber(A))