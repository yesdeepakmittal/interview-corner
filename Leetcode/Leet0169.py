#https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        mx = 0
        for key,value in d.items():
            if value > mx:
                mx = value
                k = key
        return k

    
    #Boyer-Moore Majority Voting Algorithm  | TC - O(N) | SC - O(1)
    #without using extra space - Majorith element must exist
        # if majority element does not exist always, check frequency of maj ele > n/2
        # ele = A[0]
        # freq = 1

        # for i in A[1:]:
        #     if i == ele:
        #         freq += 1
        #     else:
        #         if freq == 0:
        #             ele = i 
        #         else:
        #             freq -= 1
        # return ele