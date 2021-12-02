// TC - O(N) | SC - O(1) - #varibles constant & independent of size of array
public class ElementsGreaterThanItself{
    public static void main(String[] args){
        int[] arr = {0,3,1,2,6,9,3};
        int max = FindMax(arr);
        int cnt = CountMax(arr,max);
        System.out.println(arr.length - cnt);
    }

    static int CountMax(int[] arr, int max) {
        int cnt = 0;
        for(int i = 0; i<arr.length; i++){
            if(arr[i] == max){
                cnt++;
            }
        }
        return cnt;
    }

    static int FindMax(int[] arr) {
        int max = arr[0];
        for(int i = 0; i < arr.length; i++){
            if(arr[i] > max){
                max = arr[i];
            }
        }
        return max;
    }
}