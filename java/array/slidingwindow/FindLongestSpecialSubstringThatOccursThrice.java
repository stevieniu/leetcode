/**
 * 2981. Find Longest Special Substring That Occurs Thrice I
 * https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/description/
 *
 * You are given a string s that consists of lowercase English letters.
 *
 * A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.
 *
 * Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.
 *
 * A substring is a contiguous non-empty sequence of characters within a string.
 *
 *
 *
 * Example 1:
 *
 * Input: s = "aaaa"
 * Output: 2
 * Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
 * It can be shown that the maximum length achievable is 2.
 * Example 2:
 *
 * Input: s = "abcdef"
 * Output: -1
 * Explanation: There exists no special substring which occurs at least thrice. Hence return -1.
 * Example 3:
 *
 * Input: s = "abcaba"
 * Output: 1
 * Explanation: The longest special substring which occurs thrice is "a": substrings "abcaba", "abcaba", and "abcaba".
 * It can be shown that the maximum length achievable is 1.
 *
 *
 * Constraints:
 *
 * 3 <= s.length <= 50
 * s consists of only lowercase English letters.
 */
package array.slidingwindow;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class FindLongestSpecialSubstringThatOccursThrice {
    public static void main(String[] args) {
        String s = "eccdnmcnkl";
        new FindLongestSpecialSubstringThatOccursThrice().maximumLength(s);
    }
    public int maximumLength(String s) {
        var groups = new HashMap<Character, List<Integer>>();
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if ( i == 0 || c != s.charAt(i - 1) ) {
                var lst = groups.containsKey(c) ? groups.get(c) : new ArrayList<Integer>();
                lst.add(1);
                groups.put(c, lst);
            } else {
                var lst = groups.get(c);
                lst.set(lst.size() - 1, lst.get(lst.size() - 1) + 1);
            }
        }
        for (char key : groups.keySet()) {
            Collections.sort(groups.get(key), Collections.reverseOrder());
        }

        int res = -1;
        for (char ch = 'a'; ch <= 'z'; ch++ ) {
            if(!groups.containsKey(ch)) continue;
            List<Integer> gprs = groups.get(ch);
            int ans = gprs.get(0) - 2;
            if (gprs.size() == 2) {
                if (gprs.get(1)  + 1 >= gprs.get(0)) {
                    ans = Math.max(ans, gprs.get(0) - 1);
                }
            } else if (gprs.size() >= 3) {
                if(gprs.get(0) == gprs.get(1) && gprs.get(1) == gprs.get(2)) {
                    ans = Math.max(ans, gprs.get(0));
                } else if (gprs.get(1) + 1 >= gprs.get(0)) {
                    ans = Math.max(ans, gprs.get(0) - 1);
                }
            }
            if(ans > 0) {
                res = Math.max(res, ans);
            }

        }
        return res;
    }
}
