''''
Make all bulbs light up 
If you set any bulb, all bulbs to the right become inverse

i/p A = [0, 1, 0, 1] -> 4
[1 0 1 0]
[1 1 0 1]
[1 1 1 0]
[1 1 1 1]

A = [1,1,1,1] -> 0
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        cnt = 0
        # for i in range(len(A)):
        #     if A[i] != 1:
        #         cnt += 1
        #         for j in range(i+1,len(A)):
        #             A[j] = A[j] ^ 1
        # return cnt

        ''''
        cnt %2 == 0 - means bulbs are now on initial state
        if A[i] == 0 and cnt%2 != 0 means it is inverted and no need to count for that case
        '''

        for i in range(len(A)):
            if A[i] == 1 and cnt %2 == 0: 
                continue
            elif A[i] == 0 and cnt%2 != 0:
                continue
            elif A[i] == 1 and cnt%2 != 0:
                cnt += 1
            elif A[i] == 0 and cnt % 2 == 0:
                cnt += 1
        return cnt

print(Solution().bulbs([0,1,0,1]))