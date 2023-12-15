package is.mojca.aoc2023;

import java.io.IOException;
import java.util.Arrays;

import static is.mojca.aoc2023.ReadInput.readInput;

public class Day09 {
    public static void main(String[] args) throws IOException {

        //String[] input = {"0 3 6 9 12 15","1 3 6 10 15 21","10 13 16 21 30 45"};
        String[] input = readInput(9);

        int total = 0;
        for (String line : input) {
            System.out.println(line);

            int[] history = Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
            total += predictDifference(history);
        }
        System.out.println("\n" + total);

    }

    public static int predictDifference(int[] ints) {
        int[] newRow = new int[ints.length - 1];

        for (int i = 1; i < ints.length; i++) {
            newRow[i - 1] = ints[i] - ints[i - 1];
            //System.out.println(newRow[i-1]);
        }
        // Use new array to check if all 0, if so finish recursion
        if (Arrays.equals(newRow, new int[newRow.length])) {
            return ints[ints.length - 1];
        } else {
            // Recursive call to add last numbers of each line
            return ints[ints.length - 1] + predictDifference(newRow);
        }
    }

}