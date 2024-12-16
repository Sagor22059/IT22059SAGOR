import java.util.Scanner;

public class Divisibility {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input size of array N
        int N = sc.nextInt();

        // Read all N elements and store the last number's last digit
        int lastDigit = 0;
        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            if (i == N - 1) {  // Check only the last element
                lastDigit = num % 10;  // Get the last digit
            }
        }

        // Check divisibility by 10
        if (lastDigit == 0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

        sc.close();
    }
}