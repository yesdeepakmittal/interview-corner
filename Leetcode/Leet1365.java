//https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] arr = new int[nums.length];
        for(int i = 0; i< nums.length; i++){
            for(int j = 0; j<nums.length; j++){
                if((i!=j) && (nums[j] < nums[i])){
                    arr[i] += 1;
                }
            }
        } return arr;
    }
}