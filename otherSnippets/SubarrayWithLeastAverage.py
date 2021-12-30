''''
Return first index of subarray(of length k) with least average

Sliding window technique
TC - O(N) | SC - O(1)
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self,arr,k):
        sm = sum(arr[:k])
        avg = sm/k
        ans = 0
        n = len(arr)
        
        for i in range(k,n):
            sm += arr[i]
            sm -= arr[i-k]
            if sm/k < avg:
                avg = sm/k
                ans = i-k+1
        return ans
