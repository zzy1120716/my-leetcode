"""
5. 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


# 方法一：暴力法（超时）
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        ans = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if j - i + 1 > max_len and self.isPalindrome(s, i, j):
                    ans = s[i:j + 1]
                    max_len = j - i + 1
        return ans

    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


# 方法二：中心扩展法
# 回文中心的两侧互为镜像。因此，回文可以从它的中心展开，并且只有 2n - 1 个这样的中心。
# 你可能会问，为什么会是 2n - 1 个，而不是 n 个中心？
# 原因在于所含字母数为偶数的回文的中心可以处于两字母之间（例如 “abba” 的中心在两个‘b’之间）。
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        start, end = 0, 0
        for i in range(len(s)):
            uni_center_len = self.expendAroundCenter(s, i, i)       # 单中心回文
            bi_center_len = self.expendAroundCenter(s, i, i + 1)    # 双中心回文
            better_len = max(uni_center_len, bi_center_len)
            if better_len > end - start:    # 根据中心坐标和回文串长度，推出两个端点坐标
                start = i - (better_len - 1) // 2
                end = i + better_len // 2
        return s[start:end + 1]

    def expendAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1     # 注意此处返回长度不应包括两端字符，因此，比 right - left + 1 少2，即 right - left - 1


# 方法三：动态规划
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        max_len = 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        # 长度为1的回文子串
        for i in range(n):
            dp[i][i] = True
            max_len = 1
            ans = s[i]
        # 长度为2的回文子串
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = s[i:i + 2]
                max_len = 2
        # 递推
        for j in range(n):
            for i in range(j - 1):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if max_len < j - i + 1:
                        ans = s[i:j + 1]
                        max_len = j - i + 1
        return ans


# 方法三升级版：省略初始化dp数组的两个循环
class Solution3:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for i in range(len(s))]
        ans = ""
        max_length = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    if ans == "" or max_length < j - i + 1:
                        ans = s[i:j+1]
                        max_length = j - i + 1
        return ans


if __name__ == '__main__':
    print(Solution2().longestPalindrome("babad"))
    print(Solution2().longestPalindrome("bab"))
    print(Solution2().longestPalindrome("a"))
