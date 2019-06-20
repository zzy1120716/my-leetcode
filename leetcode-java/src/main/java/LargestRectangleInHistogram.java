import java.util.Stack;

/**
 * 84. Largest Rectangle in Histogram
 * Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
 *
 * Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
 *
 * The largest rectangle is shown in the shaded area, which has area = 10 unit.
 *
 * Example:
 *
 * Input: [2,1,5,6,2,3]
 * Output: 10
 **/
public class LargestRectangleInHistogram {

    /**
     * The main function to find the maximum rectangular area under given
     * @param heights 直方图
     * @return 最大面积
     */
    public int largestRectangleArea(int[] heights) {

        // Create an empty stack. The stack holds indexes of hist[] array
        // The bars stored in stack are always in increasing order of their
        // heights.
        Stack<Integer> stack = new Stack<>();

        int n = heights.length;
        int maxArea = 0;    // Initialize max area
        int tp; // To store top of stack
        int areaWithTop;    // To store area with top bar as the smallest bar

        // Run through all bars of given histogram
        int i = 0;
        while (i < n) {
            // If this bar is higher than the bar on top stack, push it to stack
            if (stack.empty() || heights[stack.peek()] <= heights[i]) {
                stack.push(i++);
            } else {
                // If this bar is lower than top of stack, then calculate area of rectangle
                // with stack top as the smallest (or minimum height) bar. 'i' is
                // 'right index' for the top and element before top in stack is 'left index'
                tp = stack.peek();  // store the top index
                stack.pop();    // pop the top

                // Calculate the area with hist[tp] stack as smallest bar
                areaWithTop = heights[tp] * (stack.empty() ? i : i - stack.peek() - 1);

                // update max area, if needed
                maxArea = Math.max(maxArea, areaWithTop);
            }
        }

        // Now pop the remaining bars from stack and calculate area with every
        // popped bar as the smallest bar
        while (!stack.empty()) {
            tp = stack.pop();
            areaWithTop = heights[tp] * (stack.empty() ? i : i - stack.peek() - 1);

            maxArea = Math.max(maxArea, areaWithTop);
        }

        return maxArea;
    }

    public static void main(String[] args) {
        int[] heights = {2, 1, 5, 6, 2, 3};
        System.out.println(new LargestRectangleInHistogram().largestRectangleArea(heights));
    }
}
