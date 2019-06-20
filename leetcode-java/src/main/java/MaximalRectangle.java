/**
 * 85. Maximal Rectangle
 * Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
 *
 * Example:
 *
 * Input:
 * [
 *   ["1","0","1","0","0"],
 *   ["1","0","1","1","1"],
 *   ["1","1","1","1","1"],
 *   ["1","0","0","1","0"]
 * ]
 * Output: 6
 **/
public class MaximalRectangle {

    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0) return 0;
        // for each cell with value=1, we look upward (north), the number of continuous '1' is the height of cell
        int[] heights = new int[matrix[0].length];
        int maxArea = -1;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == '0') {
                    heights[j] = 0;
                } else {
                    heights[j]++;
                }
            }

            // 利用84题的代码
            int area = new LargestRectangleInHistogram().largestRectangleArea(heights);
            maxArea = Math.max(maxArea, area);
        }
        return maxArea;
    }

    public static void main(String[] args) {
        char[][] matrix = {{'1','0','1','0','0'},
                            {'1','0','1','1','1'},
                            {'1','1','1','1','1'},
                            {'1','0','0','1','0'}};
        System.out.println(new MaximalRectangle().maximalRectangle(matrix));
    }
}
