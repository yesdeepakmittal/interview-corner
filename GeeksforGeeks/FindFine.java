
// https://practice.geeksforgeeks.org/problems/find-the-fine4353/1/
class Solution {
    
    public long totalFine( long n, long date, long car[], long fine[])
    {
        long oddFine = 0;
        long evenFine = 0;
        
        for(int i = 0; i < n; i++){
            if(car[i] % 2 == 0){
                evenFine += fine[i];
            }
            else{
                oddFine += fine[i];
            }
        }
        
        if(date % 2 == 0){
            return oddFine;
        }
        else{
            return evenFine;
        }
        
    }
}