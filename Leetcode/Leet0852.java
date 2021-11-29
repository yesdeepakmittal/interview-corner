//https://leetcode.com/problems/peak-index-in-a-mountain-array/
class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        //binary search approach - 0(logN)
        int start = 0;
        int end = arr.length - 1;
        while(start < end){
            int mid = start + (end-start)/2;
            if(arr[mid]>arr[mid+1]){
                end = mid; //u r in decreasing part
            }
            else{
                start = mid + 1; //u r in increasng part
            }
        } return start; //or end as start == end now
    }
}