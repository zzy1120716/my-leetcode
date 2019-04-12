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


class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        la = [int(d) for d in a]
        lb = [int(d) for d in b]
        res = []
        len_a, len_b = len(a), len(b)
        carry = 0
        while len_a > 0 and len_b > 0:
            da, db = la.pop(), lb.pop()
            res.append((da + db + carry) % 2)
            carry = (da + db + carry) // 2
            len_a -= 1
            len_b -= 1
        while len_a > 0:
            da = la.pop()
            res.append((da + carry) % 2)
            carry = (da + carry) // 2
            len_a -= 1
        while len_b > 0:
            db = lb.pop()
            res.append((db + carry) % 2)
            carry = (db + carry) // 2
            len_b -= 1
        if carry:
            res.append(carry)
        return ''.join([str(c) for c in res])[::-1]


if __name__ == '__main__':
    # print(Solution1().addBinary('1010', '1011'))
    print(Solution1().addBinary('11', '1'))
