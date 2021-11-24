# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
    
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # l = []
        # for index,value in enumerate(nums):
        #     if value == target:
        #         l.append(index)
        # if len(l) == 1: return l*2
        # elif len(l) > 1: return [l[0],l[-1]]
        # else: return [-1,-1]
        #this is not a binary search(O(logn)) 
        
        
        def searchIndex(nums,target,firstIndex):
            ans = -1
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = start + (end-start)//2
                if target < nums[mid]:
                    end = mid - 1
                elif target > nums[mid]:
                    start = mid + 1
                else:
                    ans = mid
                    if firstIndex:
                        end= mid - 1
                    else:
                        start = mid + 1
            return ans
        
        l = [-1,-1]
        l[0] = searchIndex(nums,target,True)
        l[-1] = searchIndex(nums,target,False)
        return l
    
        