import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws Exception {
    Scanner scn = new Scanner(System.in);
    int n = scn.nextInt();
    int[][] arr = new int[n][n];
    for (int i = 0; i < arr.length; i++) {
      for (int j = 0; j < arr[0].length; j++) {
        arr[i][j] = scn.nextInt();
      }
    }
    // transpose
    for (int i = 0; i < arr.length; i++) {
      for (int j = i; j < arr[0].length; j++) {
        int temp = arr[i][j];
        arr[i][j] = arr[j][i];
        arr[j][i] = temp;
      }
    }

    // reverse the columns
    for (int i = 0; i < arr.length; i++ ) {
      int left = 0;
      int right = arr.length - 1;
      while (left < right) {
        int temp = arr[i][left];
        arr[i][left] = arr[i][right];
        arr[i][right] = temp;
        left++;
        right--;
      }

    }

    display(arr);


  }

  public static void display(int[][] arr) {
    for (int i = 0; i < arr.length; i++) {
      for (int j = 0; j < arr[0].length; j++) {
        System.out.print(arr[i][j] + " ");
      }
      System.out.println();
    }
  }

}
