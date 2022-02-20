class Solution {
    public int[] rotate(int[] nums, int k) {
        int arr[] = new int[nums.length];
        int j = 0;
        k = k%nums.length;
        for(int i = k;i < nums.length; i++){
            arr[i] = nums[j];
            j += 1;
        }
        for(int i = 0; i < k; i++){
            arr[i] = nums[j];
            j += 1;
        }
        for(int i = 0; i < nums.length; i++){
            nums[i] = arr[i];
        }
        return nums;
    }
}