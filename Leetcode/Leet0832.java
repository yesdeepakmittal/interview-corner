//https://leetcode.com/problems/flipping-an-image/
class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        int[][] arr = new int[image.length][image.length];
        for(int row=0; row < image.length; row++){
            for(int col=0; col < image[row].length; col++){
            arr[row][col] = image[row][image[row].length - 1 - col]; //reverse
            arr[row][col] = arr[row][col] == 1?0:1; //invert
            }
        }return arr;
    }
}