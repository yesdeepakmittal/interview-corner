class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        List<Integer> list = new ArrayList<Integer>();
        for(int i = 0; i< nums.length; i++){
            list.add(index[i],nums[i]);
        }
        
        int[] ans = new int[nums.length];
        for(int i = 0; i<nums.length; i++){
            ans[i] = list.get(i);
        }return ans;
    }
}