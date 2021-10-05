import java.io.*;
import java.util.*;

public class Main{

public static void main(String[] args) throws Exception {
    Scanner scn= new Scanner(System.in);
    int n= scn.nextInt(); // number of rows
    int m= scn.nextInt(); // number of columns
    
    int[][] arr= new int[n][m];
    
    for(int i=0; i<n;i++) {
        for(int j=0;j<m;j++){
            arr[i][j]= scn.nextInt();
        }
    }
    
    for(int j=0;j<m;j++){
        if(j%2==0){  // if columns is even 
            for(int i=0;i<n;i++){
                System.out.println(arr[i][j]);
            }
        }
        else {  // if column is odd
            for(int i=n-1; i>=0;i--) {
                 System.out.println(arr[i][j]);
            }
        }
    }
 }

}
