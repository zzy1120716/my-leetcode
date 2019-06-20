import java.util.*;

/**
 * 126. Word Ladder II
 *
 * Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
 *
 * Only one letter can be changed at a time
 * Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
 * Note:
 *
 * Return an empty list if there is no such transformation sequence.
 * All words have the same length.
 * All words contain only lowercase alphabetic characters.
 * You may assume no duplicates in the word list.
 * You may assume beginWord and endWord are non-empty and are not the same.
 *
 * Example 1:
 *
 * Input:
 * beginWord = "hit",
 * endWord = "cog",
 * wordList = ["hot","dot","dog","lot","log","cog"]
 *
 * Output:
 * [
 *   ["hit","hot","dot","dog","cog"],
 *   ["hit","hot","lot","log","cog"]
 * ]
 *
 * Example 2:
 *
 * Input:
 * beginWord = "hit"
 * endWord = "cog"
 * wordList = ["hot","dot","dog","lot","log"]
 *
 * Output: []
 *
 * Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
 **/

// 迭代加深搜索
class WordLadderII2 {

    Map<String, List<String>> graph = new HashMap<>();
    List<List<String>> ans = new ArrayList<>();
    // word到end至少需要多少步，即lower bound，下界
    Map<String, Integer> lb = new HashMap<>();

    // TODO... naive dfs方法超时，考虑剪枝
    // 当前word离end至少还有多少步 ==> 比较word和end有几个字母不同
    private void dfs(int limit, int x, String word, String end, List<String> path) {

        // 此处为什么用limit + 1？
        // 因为，x是即将要做的变换
        if (x == limit + 1) {
            if (word.equals(end)) {					//如果当前单词和end相同
                // deep copy
                ans.add(new ArrayList<>(path));		//答案将当前path存入
            }
            return;
        }

        // 剪枝：如果上一次迭代的数量 + 下界 > 迭代上限，
        // 则一定得不到满足条件的路径，直接返回
        if (x - 1 + lb.get(word) > limit) {     //如果当前单词的变换次数加上不同的字母数超出限制就退出
            return;
        }

        for (String next : graph.get(word)) {
            path.add(next);						//将下一个单词加入path
            dfs(limit, x + 1, next, end, path);  //继续搜索
            path.remove(path.size() - 1);        //搜索完成后删除
        }

        // 剪枝：动态更新下界
        // 代码了到这里，说明从word出发的所有路径都试完了
        // 如果ans仍为空，则说明从word出发的所有路都无法到达终点
        if (ans.isEmpty()) {
            // word走了limit - (x - 1)步，未到达终点
            // 可以更新下界
            lb.put(word, Math.max(lb.get(word), limit - (x - 1) + 1));
        }
    }

    private List<String> getNext(String word, Set<String> dict) {
        List<String> ret = new ArrayList<>();

        // 把每一位都从a-z进行修改，如果包含在dict，就添加到结果list中返回
        for (int i = 0; i < word.length(); i++) {  	//枚举当前单词替换位置
            char[] sc = word.toCharArray();
            for (char c = 'a'; c <= 'z'; c++) {      //枚举当前可替换字母
                sc[i] = c;
                String next = String.valueOf(sc);
                if (dict.contains(next) && !word.equals(next)) {   //如果替换字母后的单词在dict中
                    ret.add(next);                                 //加入ret中
                }
            }
        }
        return ret;
    }

    // 返回两个长度相等的字符串，不同的字母的数量
    private int getDiff(String a, String b) {
        int ret = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                ret++;
            }
        }
        return ret;
    }

    public List<List<String>> findLadders(String start, String end, List<String> wordList) {

        // 构建图
        Set<String> dict = new HashSet<>(wordList);
        dict.add(start);
        dict.add(end);
        for (String word : dict) {
            graph.put(word, getNext(word, dict)); //存入当前单词和下一步方案
            // 剪枝：得到下界
            lb.put(word, getDiff(word, end));
        }

        int limit = 0;
        List<String> path = new ArrayList<>();
        path.add(start);

        while (ans.isEmpty()) {
            dfs(limit, 1, start, end, path);    //开始搜索
            limit++;							//每一步limit++
        }

        return ans;
    }


    public static void main(String[] args) {
        List<String> wordList = new ArrayList<>();
        wordList.add("hot");
        wordList.add("dot");
        wordList.add("dog");
        wordList.add("lot");
        wordList.add("log");
        wordList.add("cog");
        System.out.println(new WordLadderII2().findLadders("hit", "cog", wordList));

        List<String> wordList2 = new ArrayList<>();
        wordList2.add("hot");
        wordList2.add("dot");
        wordList2.add("dog");
        wordList2.add("lot");
        wordList2.add("log");
        System.out.println(new WordLadderII2().findLadders("hit", "cog", wordList2));

        List<String> wordList3 = new ArrayList<>();
        wordList2.add("hot");
        wordList2.add("dog");
        System.out.println(new WordLadderII2().findLadders("hot", "dog", wordList3));
    }
}
