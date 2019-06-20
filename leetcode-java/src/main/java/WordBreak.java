import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * 139. Word Break
 *
 * Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
 *
 * Note:
 *
 * The same word in the dictionary may be reused multiple times in the segmentation.
 * You may assume the dictionary does not contain duplicate words.
 *
 * Example 1:
 *
 * Input: s = "leetcode", wordDict = ["leet", "code"]
 * Output: true
 * Explanation: Return true because "leetcode" can be segmented as "leet code".
 *
 * Example 2:
 *
 * Input: s = "applepenapple", wordDict = ["apple", "pen"]
 * Output: true
 * Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
 *              Note that you are allowed to reuse a dictionary word.
 *
 * Example 3:
 *
 * Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
 * Output: false
 **/
public class WordBreak {

    public boolean wordBreak(String s, List<String> wordDict) {
        int n = s.length();
        boolean[] visited = new boolean[n];
        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(0);
        while (!q.isEmpty()) {
            int start = q.poll();
            if (!visited[start]) {
                for (int i = start + 1; i <= n; i++) {
                    if (wordDict.contains(s.substring(start, i))) {
                        q.offer(i);
                        if (i == n) return true;
                    }
                }
                visited[start] = true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        WordBreak wordBreak = new WordBreak();
        String[] wordStrs1 = {"apple", "pen"};
        List<String> wordDict1 = Arrays.asList(wordStrs1);
        System.out.println(wordBreak.wordBreak("applepenapple", wordDict1));
    }
}
