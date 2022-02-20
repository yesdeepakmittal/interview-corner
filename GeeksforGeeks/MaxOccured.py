#https://practice.geeksforgeeks.org/problems/maximum-occured-integer4602/1/

class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self,L,R,N):
        ##Your code here  | O(N2)
        # d = {}
        # cnt = 0
        # ans = max(R)
        # for i in range(N):
        #     for j in range(L[i],R[i]+1):
        #         if j in d:
        #             d[j] += 1
        #             if d[j] >= cnt:
        #                 cnt = d[j]
        #         else:
        #             d[j] = 1

        # for k,v in d.items():
        #     if v > cnt:
        #         cnt = v
        # for k,v in d.items():
        #     if v == cnt:
        #         ans = min(ans,k)

        # return ans
        
        # Prefix Sum Approach | O(N)
        arr = [0 for i in range(max(R) + 1 + 1)]
        for i in range(N):
            arr[L[i]] += 1
            arr[R[i] + 1] -= 1
        
        for i in range(1,len(arr)):
            arr[i] = arr[i-1] + arr[i]
        
        return arr.index(max(arr))


L = [2, 1, 3]
R = [5, 3, 9]

print(Solution().maxOccured(L,R,len(L)))