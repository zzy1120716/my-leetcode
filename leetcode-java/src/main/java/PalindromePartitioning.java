import java.util.ArrayList;
import java.util.List;

/**
 * 131. Palindrome Partitioning
 *
 * Given a string s, partition s such that every substring of the partition is a palindrome.
 *
 * Return all possible palindrome partitioning of s.
 *
 * Example:
 *
 * Input: "aab"
 * Output:
 * [
 *   ["aa","b"],
 *   ["a","a","b"]
 * ]
 **/
public class PalindromePartitioning {

    public List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<List<String>>();
        List<String> path = new ArrayList<String>();
        helper(s, 0, path, res);
        return res;
    }

    private void helper(String s, int start, List<String> path, List<List<String>> res) {
        if (start == s.length()) {
            res.add(new ArrayList<String>(path));
            return;
        }
        for (int i = start; i < s.length(); i++) {
            if (!isPalindrome(s, start, i)) continue;
            path.add(s.substring(start, i + 1));
            helper(s, i + 1, path, res);
            path.remove(path.size() - 1);
        }
    }

    private boolean isPalindrome(String s, int start, int end) {
        while (start < end) {
            if (s.charAt(start) != s.charAt(end)) return false;
            start++;
            end--;
        }
        return true;
    }

    public static void main(String[] args) {
        PalindromePartitioning palindromePartitioning = new PalindromePartitioning();
        System.out.println(palindromePartitioning.partition("aab"));
    }
}
