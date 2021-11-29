//https://leetcode.com/problems/find-peak-element/
class Solution {
    public int findPeakElement(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        while(start < end){
            int mid = start + (end - start)/2;
            if(nums[mid]> nums[mid+1]){
                //you are in decreasng part
                end = mid;
            }
            else{
                //you are in increasing part now
                start = mid + 1;
            }
        } return end; //or start as start == end
    }
}