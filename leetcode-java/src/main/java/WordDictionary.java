/**
 * 211. Add and Search Word - Data structure design
 * Design a data structure that supports the following two operations:
 *
 * void addWord(word)
 * bool search(word)
 * search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
 *
 * Example:
 *
 * addWord("bad")
 * addWord("dad")
 * addWord("mad")
 * search("pad") -> false
 * search("bad") -> true
 * search(".ad") -> true
 * search("b..") -> true
 * Note:
 * You may assume that all words are consist of lowercase letters a-z.
 **/
class WordDictionary {

    private TrieNode root;

    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isWord = false;
    }

    /** Initialize your data structure here. */
    public WordDictionary() {
        root = new TrieNode();
    }

    /** Adds a word into the data structure. */
    public void addWord(String word) {
        TrieNode p = root;
        for (int i = 0; i < word.length(); i++) {
            int idx = word.charAt(i) - 'a';
            if (p.children[idx] == null) {
                p.children[idx] = new TrieNode();
            }
            p = p.children[idx];
        }
        p.isWord = true;
    }

    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    public boolean search(String word) {
        return searchWord(word, root, 0);
    }

    private boolean searchWord(String word, TrieNode p, int i) {
        if (i == word.length()) return p.isWord;
        if (word.charAt(i) == '.') {
            for (TrieNode ch : p.children) {
                if (ch != null && searchWord(word, ch, i + 1))
                    return true;
            }
            return false;
        } else {
            return p.children[word.charAt(i) - 'a'] != null && searchWord(word, p.children[word.charAt(i) - 'a'], i + 1);
        }
    }

    public static void main(String[] args) {
        WordDictionary wordDictionary = new WordDictionary();
        wordDictionary.addWord("bad");
        wordDictionary.addWord("dad");
        wordDictionary.addWord("mad");
        System.out.println(wordDictionary.search("pad"));
        System.out.println(wordDictionary.search("bad"));
        System.out.println(wordDictionary.search(".ad"));
        System.out.println(wordDictionary.search("b.."));
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
