import java.util.*;

/**
 * 140. Word Break II
 *
 * Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
 *
 * Note:
 *
 * The same word in the dictionary may be reused multiple times in the segmentation.
 * You may assume the dictionary does not contain duplicate words.
 *
 * Example 1:
 *
 * Input:
 * s = "catsanddog"
 * wordDict = ["cat", "cats", "and", "sand", "dog"]
 * Output:
 * [
 *   "cats and dog",
 *   "cat sand dog"
 * ]
 *
 * Example 2:
 *
 * Input:
 * s = "pineapplepenapple"
 * wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
 * Output:
 * [
 *   "pine apple pen apple",
 *   "pineapple pen apple",
 *   "pine applepen apple"
 * ]
 * Explanation: Note that you are allowed to reuse a dictionary word.
 *
 * Example 3:
 *
 * Input:
 * s = "catsandog"
 * wordDict = ["cats", "dog", "sand", "and", "cat"]
 * Output:
 * []
 **/
public class WordBreakII {

    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<String>(wordDict);
        return dfs(s, wordSet, new HashMap<String, LinkedList<String>>());
    }

    private List<String> dfs(String s, Set<String> wordSet, HashMap<String, LinkedList<String>> memo) {
        if (memo.containsKey(s))
            return memo.get(s);

        LinkedList<String> res = new LinkedList<String>();
        if (s.length() == 0) {
            res.add("");
            return res;
        }

        for (String word : wordSet) {
            if (s.startsWith(word)) {
                List<String> sublist = dfs(s.substring(word.length()), wordSet, memo);
                for (String sub : sublist)
                    res.add(word + (sub.isEmpty() ? "" : " ") + sub);
            }
        }

        memo.put(s, res);
        return res;
    }

    public static void main(String[] args) {
        WordBreakII wordBreakII = new WordBreakII();
        String[] wordStrs1 = {"apple", "pen", "applepen", "pine", "pineapple"};
        List<String> wordDict1 = Arrays.asList(wordStrs1);
        System.out.println(wordBreakII.wordBreak("pineapplepenapple", wordDict1));
    }
}
