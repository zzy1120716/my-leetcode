"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


# 使用dict记录字符最后出现的位置
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastOccurred = {}
        start = max_len = 0
        for i, ch in enumerate(s):
            if ch in lastOccurred and lastOccurred[ch] >= start:
                start = lastOccurred[ch] + 1
            max_len = max(max_len, i - start + 1)
            lastOccurred[ch] = i
        return max_len


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcabcbb'))
