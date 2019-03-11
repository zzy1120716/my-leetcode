"""
18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c,
and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array
which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


# 方法一：枚举一个数后，将问题转化为3Sum，注意去重
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.threeSum(nums, i, results, target - nums[i])
        return results

    def threeSum(self, nums, index, results, three_sum):
        for j in range(index + 1, len(nums) - 2):
            if j != index + 1 and nums[j] == nums[j - 1]:
                continue
            two_sum = three_sum - nums[j]
            left, right = j + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == two_sum:
                    results.append([nums[index], nums[j], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > two_sum:
                    right -= 1
                else:
                    left += 1


# 方法二：DFS，有错误
class Solution1:
    def fourSum(self, nums, target):
        results = []
        nums.sort()
        self.four_sum(nums, 0, [], results, target)
        return results

    def four_sum(self, nums, start, temp, results, target):
        if len(temp) == 4 and target == 0:
            results.append(temp.copy())
        end = start
        while end < len(nums):
            if target < nums[end]:
                break
            if end != start and nums[end] == nums[end - 1]:
                end += 1
                continue
            temp.append(nums[end])
            self.four_sum(nums, end + 1, temp, results, target - nums[end])
            temp.pop()
            end += 1


if __name__ == '__main__':
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
