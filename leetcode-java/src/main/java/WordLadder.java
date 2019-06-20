import java.util.*;

/**
 * 127. Word Ladder
 *
 * Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
 *
 * Only one letter can be changed at a time.
 * Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
 * Note:
 *
 * Return 0 if there is no such transformation sequence.
 * All words have the same length.
 * All words contain only lowercase alphabetic characters.
 * You may assume no duplicates in the word list.
 * You may assume beginWord and endWord are non-empty and are not the same.
 *
 * Example 1:
 * Input:
 * beginWord = "hit",
 * endWord = "cog",
 * wordList = ["hot","dot","dog","lot","log","cog"]
 * Output: 5
 * Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
 * return its length 5.
 *
 * Example 2:
 * Input:
 * beginWord = "hit"
 * endWord = "cog"
 * wordList = ["hot","dot","dog","lot","log"]
 * Output: 0
 * Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
 **/
public class WordLadder {

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordSet = new HashSet<String>(wordList);
        if (!wordSet.contains(endWord)) return 0;
        Queue<String> queue = new LinkedList<String>();
        queue.offer(beginWord);
        int res = 0;
        while (!queue.isEmpty()) {
            int len = queue.size();
            for (int i = 0; i < len; i++) {
                String word = queue.poll();
                if (word.equals(endWord))
                    return res + 1;
                for (int j = 0; j < word.length(); j++) {
                    String newWord = word;
                    for (char ch = 'a'; ch <= 'z'; ch++) {
                        newWord = newWord.substring(0, j) + ch + newWord.substring(j + 1);
                        if (wordSet.contains(newWord) && !newWord.equals(word)) {
                            queue.offer(newWord);
                            wordSet.remove(newWord);
                        }
                    }
                }
            }
            res++;
        }
        return 0;
    }

    public static void main(String[] args) {
        List<String> wordList = new ArrayList<String>();
        wordList.add("hot");
        wordList.add("dot");
        wordList.add("dog");
        wordList.add("lot");
        wordList.add("log");
        wordList.add("cog");
        System.out.println(new WordLadder().ladderLength("hit", "cog", wordList));
    }
}
