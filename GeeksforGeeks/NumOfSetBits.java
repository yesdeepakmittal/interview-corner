//https://practice.geeksforgeeks.org/problems/set-bits0143/1/
class Solution {
    static int setBits(int N) {
        // code here
        int cnt = 0;
        while(N > 0){
            N = N &(N-1);
            cnt++;
        }
        return cnt;
    }
}