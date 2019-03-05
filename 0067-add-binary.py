"""
67. 二进制求和

给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        tmp = ''
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            s = carry
            if j >= 0:
                s += ord(b[j]) - ord('0')
            if i >= 0:
                s += ord(a[i]) - ord('0')
            tmp += str(s % 2)
            carry = s // 2
            j -= 1; i -= 1
        if carry != 0:
            tmp += str(carry)
        return tmp[::-1]


if __name__ == '__main__':
    print(Solution().addBinary('1010', '1011'))
