import java.util.HashMap;
import java.util.Map;

/**
 * 318. Maximum Product of Word Lengths
 *
 * Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
 *
 * Example 1:
 * Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
 * Output: 16
 * Explanation: The two words can be "abcw", "xtfn".
 *
 * Example 2:
 * Input: ["a","ab","abc","d","cd","bcd","abcd"]
 * Output: 4
 * Explanation: The two words can be "ab", "cd".
 *
 * Example 3:
 * Input: ["a","aa","aaa","aaaa"]
 * Output: 0
 * Explanation: No such pair of words.
 **/
public class MaximumProductOfWordLength {

    public int maxProduct(String[] words) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        int res = 0;
        for (String word : words) {
            int mask = 0;
            for (int i = 0; i < word.length(); i++) {
                mask |= 1 << (word.charAt(i) - 'a');
            }
            map.put(mask, Math.max(map.getOrDefault(mask, 0), word.length()));
            for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
                if ((mask & entry.getKey()) == 0) {
                    res = Math.max(res, word.length() * entry.getValue());
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        MaximumProductOfWordLength maximumProductOfWordLength = new MaximumProductOfWordLength();
        String[] input1 = {"abcw", "baz", "foo", "bar", "xtfn", "abcdef"};
        String[] input2 = {"a", "ab", "abc", "d", "cd", "bcd", "abcd"};
        String[] input3 = {"a", "aa", "aaa", "aaaa"};
        System.out.println(maximumProductOfWordLength.maxProduct(input1));
        System.out.println(maximumProductOfWordLength.maxProduct(input2));
        System.out.println(maximumProductOfWordLength.maxProduct(input3));
    }
}
