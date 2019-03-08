"""
53. 最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""


# 方法一：动态规划就，O(n)
# nums: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# f:    [-2, 1, -2, 4,  3, 5, 6,  1, 5]
class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 0:
            return 0
        f = [nums[0]] + [0] * (len(nums) - 1)
        for i in range(1, len(nums)):
            f[i] = max(f[i - 1] + nums[i], nums[i])
            # if f[i - 1] > 0:
            #     f[i] = f[i - 1] + nums[i]
            # else:
            #     f[i] = nums[i]
        return max(f)


# 观察到上述f[i]只跟f[i-1]有关，并且最大值可以在循环中记录，
# 因此，有如下改进算法：
class Solution1:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 0:
            return 0
        ans = nums[0]
        pre_sum = nums[0]
        for i in range(1, len(nums)):
            pre_sum = max(pre_sum + nums[i], nums[i])
            ans = max(pre_sum, ans)
        return ans


# 方法二：DC，O(nlogn)
class Solution2:
    def maxSubArray(self, nums) -> int:
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, left, right):
        if left > right:
            return -(1 << 31) + 1
        mid = (left + right) // 2

        leftMax = sumNum = 0
        for i in range(mid - 1, left - 1, -1):
            sumNum += nums[i]
            leftMax = max(leftMax, sumNum)

        rightMax = sumNum = 0
        for i in range(mid + 1, right + 1):
            sumNum += nums[i]
            rightMax = max(rightMax, sumNum)

        leftAns = self.helper(nums, left, mid - 1)
        rightAns = self.helper(nums, mid + 1, right)

        return max(leftMax + nums[mid] + rightMax, max(leftAns, rightAns))


if __name__ == '__main__':
    # 6
    print(Solution2().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
