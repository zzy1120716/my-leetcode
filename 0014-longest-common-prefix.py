"""
14. 最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""
import sys


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        min_len = sys.maxsize
        shortest_str = ''
        for i in range(len(strs)):
            if len(strs[i]) < min_len:
                shortest_str = strs[i]
                min_len = len(shortest_str)
        lcp = ''
        flag = True
        for i in range(min_len):
            for j in range(len(strs)):
                if strs[j][i] != shortest_str[i]:
                    flag = False
            if flag:
                lcp = shortest_str[:i + 1]
        return lcp


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
