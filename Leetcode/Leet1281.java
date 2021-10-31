class Solution {
    public int subtractProductAndSum(int n) {
        int temp;
        int sum = 0;
        int prod = 1;
        while(n>0){
            temp = n%10;
            n /= 10;
            prod *= temp;
            sum  += temp;
        }
        return prod - sum;
    }
}