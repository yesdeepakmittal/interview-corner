//https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] ans = {-1,-1};
        ans[0] = searchFn(nums, target, true);
        if (ans[0] != -1) {
            ans[1] = searchFn(nums, target, false);
        }
        return ans;
    }
    
    int searchFn(int[] arr, int target, boolean startIndex){
        int ans = -1;
        int start = 0;
        int end = arr.length - 1;
        
        while(start <= end){
            int mid = start + (end-start)/2;
            
            if(target < arr[mid]){
                end = mid - 1;
            }
            else if(target > arr[mid]){
                start = mid +1;
            }
            else{
                ans = mid;
                if(startIndex){
                    end = mid - 1;
                }
                else{
                    start = mid + 1;
                }
            }
        }return ans;
    }
}