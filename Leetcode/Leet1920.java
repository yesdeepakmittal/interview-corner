class Solution {
    public int[] buildArray(int[] nums) {
        int len = nums.length;
        int[] arr = new int[len];
        for(int i =0; i<len; i++){
            arr[i] = nums[nums[i]];
        }
        return arr;
    }
}