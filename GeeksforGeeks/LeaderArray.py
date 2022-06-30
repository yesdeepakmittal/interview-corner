class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        ans = [0]*N
        mx = A[-1]
        j = N - 1
        ans[j] = mx
        
        for i in range(N-2,-1,-1):
            if A[i] >= mx:
                j -= 1
                ans[j] = A[i]
                mx = A[i]
        
        k = 0
        for i in range(N):
            if ans[i] == 0:
                k += 1
                continue
        return ans[k:]
