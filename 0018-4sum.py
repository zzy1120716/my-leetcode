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


class Solution:
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
