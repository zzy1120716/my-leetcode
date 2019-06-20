/**
 * 307. Range Sum Query - Mutable
 *
 * Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
 *
 * The update(i, val) function modifies nums by updating the element at index i to val.
 *
 * Example:
 *
 * Given nums = [1, 3, 5]
 *
 * sumRange(0, 2) -> 9
 * update(1, 2)
 * sumRange(0, 2) -> 8
 *
 * Note:
 *
 * The array is only modifiable by the update function.
 * You may assume the number of calls to update and sumRange function is distributed evenly.
 **/
public class NumArray {

    // 树状数组
    private int[] tree;
    private int n;

    public NumArray(int[] nums) {
        if (nums.length > 0) {
            n = nums.length;
            tree = new int[n * 2];
            buildTree(nums);
        }
    }

    // 1. Build segment tree
    // [2, 4, 5, 7, 8, 9]
    private void buildTree(int[] nums) {
        for (int i = n, j = 0; i < 2 * n; i++, j++) {
            // [0, 0, 0, 0, 0, 0, 2, 4, 5, 7, 8, 9]
            tree[i] = nums[j];
        }
        for (int i = n - 1; i > 0; --i) {
            // [35, 35, 29, 6, 12, 17, 2, 4, 5, 7, 8, 9]
            tree[i] = tree[i * 2] + tree[i * 2 + 1];
        }
    }

    // 2. Update segment tree
    // 自底向上，先更新叶子结点
    public void update(int pos, int val) {
        // pos = 5, val = 10 (9 --> 10)
        pos += n;   // 11
        tree[pos] = val;    // [0, 35, 29, 6, 12, 17, 2, 4, 5, 7, 8, 10]
        while (pos > 0) {
            int left = pos; // 11 5
            int right = pos;    // 11 5
            if (pos % 2 == 0) {
                right = pos + 1;
            } else {
                left = pos - 1; // 10 4 0
            }

            // 父结点在子结点之后更新
            tree[pos / 2] = tree[left] + tree[right];
            // [0, 35, 29, 6, 12, 18, 2, 4, 5, 7, 8, 10]
            // [0, 35, 30, 6, 12, 18, 2, 4, 5, 7, 8, 10]
            // [36, 36, 30, 6, 12, 18, 2, 4, 5, 7, 8, 10]
            pos /= 2;   // 5 2 1
        }
    }

    public int sumRange(int l, int r) {
        // 获取值为'l'的叶子
        l += n;
        // 获取值为'r'的叶子
        r += n;
        int sum = 0;
        while (l <= r) {
            if ((l % 2) == 1) {
                sum += tree[l];
                l++;
            }
            if ((r % 2 == 0)) {
                sum += tree[r];
                r--;
            }
            l /= 2;
            r /= 2;
        }
        return sum;
    }

    public static void main(String[] args) {
        int[] nums = {2, 4, 5, 7, 8, 9};
        NumArray numArray = new NumArray(nums);
        System.out.println(numArray.sumRange(0, 5));
        numArray.update(5, 10);
        System.out.println(numArray.sumRange(0, 5));
    }
}
