"""
405. Convert a Number to Hexadecimal

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:
All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero
character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.

Example 1:
Input:
26

Output:
"1a"

Example 2:
Input:
-1

Output:
"ffffffff"
"""


class Solution:
    def toHex(self, num: int) -> str:
        ans = ''
        if num == 0:
            return '0'
        # 负数先变补码
        if num < 0:
            num = 0xffffffff + 1 + num
        while num:
            adding = num % 16
            num //= 16
            ans += str(adding if adding < 10 else chr(ord('a') + adding % 10))
        return ans[::-1]


if __name__ == '__main__':
    print(Solution().toHex(-1))
