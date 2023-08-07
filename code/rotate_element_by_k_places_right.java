import java.util.*;

class Solution {
    public static void main(String[] args) {

        int[] arr = {1,2,3,4,5,6,7};
        int k = 3;
        
        rotate(arr, k);
        
    }

    public static void rotate(int[] arr, int k) {
        
        int n = arr.length;
        k = k % n;

        arr = reverseFn(arr, 0, n - k - 1);
        arr = reverseFn(arr, n - k, n - 1);
        arr = reverseFn(arr, 0, n - 1);

        System.out.println(Arrays.toString(arr));
    }

    static int[] reverseFn(int[] arr, int start, int end){
        while(start < end){
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;

            start += 1;
            end -= 1; 
        }
        return arr;
    }
}