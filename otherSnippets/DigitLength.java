public class DigitLength{
    public static void main(String[] args) {
        int num = 34567;
        int len = (int)Math.log10(num) + 1;
        System.out.println("The length of a given integer is "+ len);
    }
}