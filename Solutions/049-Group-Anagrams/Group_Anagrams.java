import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {

    public static void main(String[] args) {
        String[] cases = {"eat", "tea", "tan", "ate", "nat", "bat"};
        List<List<String>> res = new Solution().groupAnagrams(cases);
        System.out.println(res.toString());
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        int[] primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101};
        List<List<String>> ans = new ArrayList<>();
        Map<Integer, Integer> map = new HashMap<>();
        for (String s : strs) {
            int key = 1;
            for (char c : s.toCharArray()) {
                key *= primes[c - 'a'];
            }
            if (map.containsKey(key)) {
                ans.get(map.get(key)).add(s);
            } else {
                map.put(key, ans.size());
                List<String> t = new ArrayList<>();
                t.add(s);
                ans.add(t);
            }
        }

        return ans;
    }
}
