import java.lang.*;
import java.util.*;

public class Leet1095 {
    public static void main(String[] args) {
        int[] arr= {1,2,3,5,6,4,3};
        int target = 3;
        int peak = peakIndexInMountainArray(arr);
        int firstHalf = orderAgnosticBS(arr,target,0,peak);
        if(firstHalf != -1){
            System.out.println(firstHalf);  //return from here
        }
        System.out.println(orderAgnosticBS(arr,target,peak+1,arr.length-1));
    }

    static int peakIndexInMountainArray(int[] arr){
        int start = 0;
        int end = arr.length - 1;
        while (start < end){
            int mid = start + (end-start)/2;
            if(arr[mid]>arr[mid+1]){
                //you are in decreasing part
                end = mid;
            }
            else{
                // you are in increasing part
                start = mid + 1;
            }
        }return start;
    }

    static int orderAgnosticBS(int[] arr, int target,int start, int end){
//        int start = 0;
//        int end = arr.length -1 ;
        boolean isAsc = arr[start] < arr[end];
        while(start <= end){
            int mid = start + (end - start)/2;
            if(target == arr[mid]){
                return mid;
            }
            if(isAsc) {
                //array is sorted in ascending order
                if (target > arr[mid]) {
                    //remove the left part
                    start = mid + 1;
                } else if (target < arr[mid]) {
                    //remove the right part
                    end = mid - 1;
                } else {
                    return mid;
                }
            }
            else{
                //array is sorted in descending order
                if (target < arr[mid]) {
                    //remove the right part
                    start = mid + 1;
                } else if (target > arr[mid]) {
                    //remove the left part
                    end = mid - 1;
                } else {
                    return mid;
                }
            }
        }return -1;
    }
}