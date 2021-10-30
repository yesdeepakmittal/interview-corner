//https://leetcode.com/problems/richest-customer-wealth/
public class Leet1672 {
    public int maximumWealth(int[][] accounts) {
        int max = 0;
        for(int i = 0; i<accounts.length; i++){
            int temp = 0;
            for(int j = 0; j<accounts[i].length; j++){
                temp += accounts[i][j];
            }
            if(temp > max){
                max = temp;
            }
        }return max;
    }
}
