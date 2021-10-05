import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        Scanner scn= new Scanner(System.in);
        int n = scn.nextInt();
        int m= scn.nextInt();
        
        int[][] arr= new int[n][m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                arr[i][j]= scn.nextInt();
            }
        }
         
         int minrow=0; // no. of minimum row
         int maxrow=n-1; // no. of maximum row
         int mincol=0; // no. of minimum column
         int maxcol=m-1; // no. of maximum column
         int count=1;
         int total= n*m; // total number of elements in matrix
         
         while(count<=total){
             
             
            //left wall, downward
            if(count<total){
         for(int i=minrow;i<=maxrow;i++){
             System.out.println(arr[i][mincol]);
             count++;
         } 
            }
         mincol++;
         
         // bottom wall, rightward
          if(count<total){
         for(int j=mincol;j<=maxcol;j++){
             System.out.println(arr[maxrow][j]);
             count++;
         }
          }
         maxrow--;
         
         // right wall, upward
          if(count<total){
         for(int i=maxrow;i>=minrow;i--){
             System.out.println(arr[i][maxcol]);
             count++;
         }
          }
         maxcol--;
         
         // top wall, lefttward
          if(count<total){
         for(int j=maxcol;j>=mincol;j--){
             System.out.println(arr[minrow][j]);
             count++;
         }
          }
         minrow++;
         
         }
         
    }

}
