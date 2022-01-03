class Solution:
    def candy(self, A: List[int]) -> int:
        temp = [1]*len(A)
        for i in range(1,len(A)):
            if A[i] > A[i-1]:
                temp[i] = temp[i-1]+1
        for i in range(len(A)-2,-1,-1):
            if A[i] > A[i+1]:
                temp[i] = max(temp[i],temp[i+1]+1)
        return sum(temp)
        