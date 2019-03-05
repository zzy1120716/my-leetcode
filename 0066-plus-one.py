"""
66. 加一

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""


# 只有输入数组的每个元素都是9时，才会执行到最后两行，
# 其他任何情况，都会在循环中直接返回。
class Solution:
    def plusOne(self, digits):
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits = [1] + digits
        return digits


# 利用python中的列表生成式
class Solution1:
    def plusOne(self, digits):
        n = len(digits)
        num = 0
        for i in range(n):
            num += digits[i] * pow(10, n - i - 1)
        return [int(i) for i in str(num + 1)]


# TODO 递归进位


if __name__ == '__main__':
    print(Solution1().plusOne([9, 9, 9, 9]))
    print(Solution1().plusOne([4, 3, 9, 9]))
    print(Solution1().plusOne([4, 3, 2, 1]))

