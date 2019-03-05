"""
4. 寻找两个有序数组的中位数

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""
import sys


# 在小数组上做二分查找，时间O(log(min(m,n)))
# https://www.youtube.com/watch?v=LPFhl65R7ww
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # 保持对元素少的数组做二分
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        x = len(nums1)
        y = len(nums2)
        low, high = 0, x
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            # 如果partitionX为0，表示左侧没有数，maxLeftX使用-INF
            # 如果partitionX是输入数组长度，表示右侧没有数，minRightX使用+INF
            maxLeftX = -sys.maxsize if partitionX == 0 else nums1[partitionX - 1]
            minRightX = sys.maxsize if partitionX == x else nums1[partitionX]
            maxLeftY = -sys.maxsize if partitionY == 0 else nums2[partitionY - 1]
            minRightY = sys.maxsize if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # 得到正确的分区，之后根据全部元素数量是奇/偶，采用不同方式得到中位数：
                # 若为偶数，则求左侧最大值和右侧最小值的平均；
                # 若为奇数，则求左侧的最大值作为中位数；
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            # nums1划分位置太靠右，游标x向左
            elif maxLeftX > minRightY:
                high = partitionX - 1
            # nums1划分位置太靠左，游标x向右
            else:
                low = partitionX + 1


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 3, 8, 9, 15], [7, 11, 19, 21, 18, 25]))     # 11
