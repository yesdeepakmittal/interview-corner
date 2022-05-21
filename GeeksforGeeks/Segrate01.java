//https://practice.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1/
class Solution {
    void segregate0and1(int[] arr, int n) {
        // code here
        int cnt = 0;
        for(int i = 0; i < n; i++){
            if(arr[i] == 1){
                cnt++;
            }
        }
        for(int i = 0; i <n ;i++){
            if(i < (n - cnt)){
            arr[i] = 0;
            }
            else{
                arr[i] = 1;
            }
        }
        // return arr;
        
    }

}