import java.util.* ;
import java.io.*; 

public class LargestElement {

    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5};

        int larValue = largestElement(arr, arr.length);

        System.out.println("Largest Value::: " + larValue);
    }

    static int largestElement(int[] arr, int n) {
        // int largest = 0;
        int largest = Integer.MIN_VALUE;


        for(int i = 0; i < n; i++){
            if(arr[i] > largest){
                largest = arr[i];
            }
        }
        return largest;
    }
}