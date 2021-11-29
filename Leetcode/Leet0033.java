class Solution {
    public int search(int[] nums,int target){
       int pivot = FindPivot(nums);
       if(pivot == -1){
           //it is a case of simple binary search
           return binarySearch(nums,target,0,nums.length - 1);
       }
       if(nums[pivot] == target){
           return pivot;
       }
       if(nums[0] <= target){
           return binarySearch(nums,target,0,pivot-1);
       }
       else{
           return binarySearch(nums,target,pivot+1,nums.length-1);
       }
   }

   public int binarySearch(int[] arr, int target,int start,int end) {
       while(start <= end){
           //        int mid = (start + end)/2;
           int mid = start + (end - start)/2;

           if(target > arr[mid]){
               start = mid +1;
           }
           else if(target < arr[mid]){
               end = mid -1 ;
           }
           else{
               return mid;
           }
       }
       //element not found
       return -1;
   }

   public int FindPivot(int[] arr){
       int start = 0;
       int end = arr.length -1 ;
       while(start <= end){
           int mid = start + (end - start) /2 ;
           //all 4 cases
           if(mid < end && arr[mid] > arr[mid+1]){
               return mid;
           }
           if(start < mid  && arr[mid] < arr[mid-1]){
               return mid -1;
           }
           if(arr[start] >= arr[mid]){
               end = mid - 1;
           }
           else{
               start = mid + 1;
           }
       }return -1;
   }
}