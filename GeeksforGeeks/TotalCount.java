//https://practice.geeksforgeeks.org/problems/total-count2415/1/

class Solution {
    int totalCount(int[] arr, int n, int k) {
        // code here
        int ans = 0;
        int d = 0;
        int r = 0;
        
        for(int i = 0; i < n ; i++){
            d = arr[i] / k;
            r = arr[i] % k;
            
            ans += d;
            if (r > 0){
                ans++;
            }
        }
        return ans;
    }
}