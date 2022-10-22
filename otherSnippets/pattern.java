package Patterns;

public class pattern {
    public static void main(String[] args) {
        pattern10(6);
    }
    static void pattern1(int n){
        /*

        *
        * * 
        * * *   
        * * * * 

         */

        for (int row = 1; row <= 4; row++) {
            for (int col = 1; col <= row; col++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    static void pattern2(int n){

        /*
         
         *
         **
         ***
         ****
         ***
         **
         * 
          
         */

        int n2 = n%2 > 0 ? n/2 + 1 : n/2;
        
        for (int row = 1; row <= n2; row++) {
            for (int col = 1; col <= row; col++) {
                System.out.print("*");
            }
            System.out.println();
        }

        for (int row = (n - n2); row > 0; row--) {
            for (int col = row; col > 0; col--) {
                System.out.print("*");
            }
            System.out.println();
        }
    }

    static void pattern3(int n){
        /*
         
           * 
          * *
         * * *
        * * * *
         * * *
          * *
           *      
          
         */
        int n2 = n%2 > 0 ? n/2 + 1 : n/2;

        //upper triangle
        for (int row = 1; row <= n2; row++) {
            // print spaces
            for (int i = 1; i <= (n2 - row); i++) {
                System.out.print(" ");
            }
            //print *
            for (int i = 0; i < row; i++) {
                System.out.print("* ");
            }
            System.out.println();
        }
        
        //lower triangle
        for (int row = (n - n2); row > 0; row--) {
            //print spaces
            for (int i = 1; i <= (n - n2 - row + 1); i++) {
                System.out.print(" ");
            }
            //print *
            for (int i = row; i > 0; i--) {
                System.out.print("* ");
            }
            System.out.println();
        }

    }

    static void pattern4(int n){

        /* 
          
                     1 
                   2 1 2
                 3 2 1 2 3
               4 3 2 1 2 3 4
             5 4 3 2 1 2 3 4 5
           6 5 4 3 2 1 2 3 4 5 6
         7 6 5 4 3 2 1 2 3 4 5 6 7 
          
          
        */
        for (int row = 1; row <= n; row++) {
            for (int spaces = n; spaces > row; spaces--) {
                System.out.print(" " + " ");
            }
            
            for (int num = row; num > 0; num--) {
                System.out.print(num + " ");
            }
            for (int i = 2; i <= row; i++) {
                System.out.print(i + " ");
            }
            System.out.println();
        }
    }

    static void pattern5(int n){
        /*
          
          0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
          0 1 1 1 1 1 1 1 1 1 1 1 1 1 0
          0 1 2 2 2 2 2 2 2 2 2 2 2 1 0
          0 1 2 3 3 3 3 3 3 3 3 3 2 1 0
          0 1 2 3 4 4 4 4 4 4 4 3 2 1 0
          0 1 2 3 4 5 5 5 5 5 4 3 2 1 0
          0 1 2 3 4 5 6 6 6 5 4 3 2 1 0
          0 1 2 3 4 5 6 7 6 5 4 3 2 1 0
          0 1 2 3 4 5 6 6 6 5 4 3 2 1 0
          0 1 2 3 4 5 5 5 5 5 4 3 2 1 0
          0 1 2 3 4 4 4 4 4 4 4 3 2 1 0
          0 1 2 3 3 3 3 3 3 3 3 3 2 1 0
          0 1 2 2 2 2 2 2 2 2 2 2 2 1 0
          0 1 1 1 1 1 1 1 1 1 1 1 1 1 0
          0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
          
          
         */
        n = n * 2;
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                int valueAtEveryIndex = Math.min(Math.min(i,j),Math.min(n-i,n-j));
                System.out.print(valueAtEveryIndex + " ");
            }
            System.out.println();
        }
    }

    static void pattern6(int n){
        /*
          
            7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
            7 6 6 6 6 6 6 6 6 6 6 6 6 6 7
            7 6 5 5 5 5 5 5 5 5 5 5 5 6 7
            7 6 5 4 4 4 4 4 4 4 4 4 5 6 7
            7 6 5 4 3 3 3 3 3 3 3 4 5 6 7
            7 6 5 4 3 2 2 2 2 2 3 4 5 6 7
            7 6 5 4 3 2 1 1 1 2 3 4 5 6 7
            7 6 5 4 3 2 1 0 1 2 3 4 5 6 7
            7 6 5 4 3 2 1 1 1 2 3 4 5 6 7
            7 6 5 4 3 2 2 2 2 2 3 4 5 6 7
            7 6 5 4 3 3 3 3 3 3 3 4 5 6 7
            7 6 5 4 4 4 4 4 4 4 4 4 5 6 7
            7 6 5 5 5 5 5 5 5 5 5 5 5 6 7
            7 6 6 6 6 6 6 6 6 6 6 6 6 6 7
            7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
     
         */
        int value = n;
        n = n * 2;
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                int valueAtEveryIndex = value - Math.min(Math.min(i,j),Math.min(n-i,n-j));
                System.out.print(valueAtEveryIndex + " ");
            }
            System.out.println();
        }
    }

    static void pattern7(int n){

        /*
          
          A
          BC
          DEF
          GHIJ
          KLMNO
          
         */
        char ch = 'A';
        for (int row = 1; row <= n; row++) {
            for (int col = 1; col <= row; col++) {
                System.out.print(ch);
                ch++;
            } System.out.println();
        }
    }

    static void pattern8(int row,int col){
        /*
          Hollow rectangle
          * * * * * * 
          *         *
          *         *
          *         *
          * * * * * *
          
         */
        for(int i = 1; i <= row; i++){
            for (int j = 1; j <= col; j++) {
                if( i == 1 || j == 1 || i == row || j == col){
                    System.out.print("* ");
                }else{
                    System.out.print("  ");
                }
            }System.out.println();
        }
    }

    static void pattern9(int n){

        /*
          
          1 
          0 1
          1 0 1
          0 1 0 1
          1 0 1 0 1
          
         */
        for (int row = 1; row <= n; row++) {
            for (int col = 1; col <= row; col++) {
                if((row + col)%2 == 0){
                    System.out.print(1 + " ");
                }else{
                    System.out.print(0 + " ");
                }
            }System.out.println();
        }
    }

    static void pattern10(int n){
        /* Butterfly Pattern
          
          *    *
          **  **
          ******
          ******
          **  **
          *    *
          
         */

         int n2 = n % 2 > 0 ? n/2 + 1 : n / 2;

         for (int row = 1; row <= n2; row++) {
            for (int col = 1; col <= row; col++) {
                System.out.print("*");
            }
            for (int col = row; col < n2; col++) {
                System.out.print("  ");
            }
            for (int col = 1; col <= row; col++) {
                System.out.print("*");
            }
            System.out.println();
         }

         for (int row = (n - n2); row >0 ; row--) {
            for (int col = row; col > 0 ; col--) {
                System.out.print("*");
            }
            for (int col = (n - n2 - row); col > 0; col--) {
                System.out.print("  ");
            }
            for (int col = row; col > 0 ; col--) {
                System.out.print("*");
            }
            System.out.println();
         }
    }

    static void pattern11(int n){
        /* Solid Rhombus
          
              ******
             ******
            ******
           ******
          ******
         ******
          
        */

        for (int row = 1; row <= n; row++) {
            //spaces
            for (int col = n - row; col > 0; col--) {
                System.out.print(" ");
            }
            // solid rhombus stars print krne hai
            for (int col = 1; col <= n; col++) {
                System.out.print("*");
            }System.out.println();
        }
    }

    static void pattern12(int n){
        /*  Hollow rhombus

             ******
            *    *
           *    *
          *    *
         *    *
        ******

        */

        for (int row = 1; row <= n; row++) {
            for (int col = (n - row); col > 0; col--) {
                System.out.print(" ");
            }
            for (int col = 1; col <= n; col++) {
                // Agar boudary ho to * nhi to white space - same as hollow rectangle
                if(col == 1 || col == n || row == 1 || row == n){
                System.out.print("*");
                }
                else{
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }

    static void pattern13(int n){
        for (int i = 0; i < n; i++) {
            
        }
    }

}
