'''
count number of pairs such that a^b = B
A = [5, 4, 10, 15, 7, 6] (distinct integers)
B = 5

o/p : cnt = 1(10^15 = 5)

 A = [3, 6, 8, 10, 15, 50]
 B = 5

 o/p : cnt = 2 ((3 ^ 6) = 5 , (10 ^ 15) = 5 )
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    '''
    a ^ b = B 
    b ^ (a ^ b) = B ^ b 
    a = B ^ b
    '''
    def solve(self, A, B):
        cnt = 0
        # TC - O(N2)
        # for i in range(len(A)):
        #     for j in range(i+1,len(A)):
        #         if A[i] ^ A[j] == B:
        #             cnt += 1
        # return cnt

        # TC - O(N2)
        # for i in A:
        #     if i^B in A:
        #         cnt += 1
        #         A.remove(i^B)
        # return cnt

        # TC - O(N2)
        # for i in A:
        #     duplicate = i^B
        #     if duplicate in A:
        #         cnt += 1
        # return cnt //2

        s = set(A)

        # TC - O(NlogN)
        # for i in s:
        #     duplicate = i ^B
        #     if duplicate in s:
        #         # s.remove(duplicate)
        #         cnt += 1
        # return cnt//2


        # TC - O(NlogN)
        for i in A: # TC - O(N)
            duplicate = i ^ B 
            if duplicate in s:  # TC - O(logN)
                cnt += 1
            else:
                s.add(i)
        return cnt//2