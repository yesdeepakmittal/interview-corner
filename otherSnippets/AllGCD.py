'''
Find original array from GCD array(any order)
[2, 2, 2, 2, 8, 2, 2, 2, 10] -> [10,8,2]
'''

temp = []
def gcd(x,y):
    if x == 0:
        return y
    else:
        return gcd(y%x,x)

def gcd_arr(arr):
    for i in range(len(arr) - 1):
        temp.append(gcd(arr[i],arr[-1]))
        temp.append(gcd(arr[i],arr[-1]))

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        if n == 1:
            return A

        A.sort(reverse=True)
        result = [A[0],A[1]]
        # temp = []
        temp.append(gcd(A[0],A[1]))
        temp.append(gcd(A[0],A[1]))

        for i in range(2,n):
            if A[i] in temp:
                temp.remove(A[i])
            else:
                result.append(A[i])
                gcd_arr(result)
        return result