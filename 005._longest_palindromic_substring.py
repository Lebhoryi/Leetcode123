# coding=utf-8
'''
@ Summary: 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
@ Update:  

@ file:    005._longest_palindromic_substring.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-8-16 下午4:00

@ github:  https://github.com/apachecn/Interview/tree/master/docs/Algorithm/Leetcode/Python
'''

import sys

###################################################
# 方法一： 强推（时间花费顺序1）
#     每个字符当做回文子串的最后一个字符，分奇偶两种情况
###################################################

class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
        start, max_len = 0, 1
        for i in range(1, len(s)):
            # 取i及i前面的 max_len+1个字符
            even = s[i-max_len:i+1]
            # 取i及i前面的 max_len+2个字符
            odd = s[i-max_len-1:i+1]
            if i-max_len >= 0 and even == even[::-1]:
                start = i-max_len
                max_len += 1
            elif i-max_len-1 >= 0 and odd == odd[::-1]:
                start = i-max_len-1
                max_len += 2

        return s[start: start + max_len]


###################################################
# 方法二： 最长公共子串(时间贼长)（时间花费顺序4）
#     反转str，str'与之前的str重合的即为最长回文字符串
#     dp[i][j] = 0 ; dp[i][j] = dp[i-1][j-1] + 1
#     ps：求出最长公共子串后，并不一定是回文串，
#         需要判断该字符串倒置前的下标和当前的字符串下标是不是匹配。
###################################################

class Solution2:
    def longestPalindrome(self, s):
        if len(s) < 2 or s == s[::-1]:
            return s
        s_inverse = s[::-1]
        # 创建一个二维矩阵
        dp = [0] * (len(s)+1)
        max_len, lcs_str = 0, ""
        for i in range(1, len(s)+1):
            for j in range(1, len(s)+1):
                if s[i-1] == s_inverse[j-1]:
                    if i == 1 or j == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len:
                    beforeRev = len(s) - j
                    if beforeRev + dp[i][j] == i:  # 判断下标是否对应
                        max_len = dp[i][j]
                        lcs_str = s[i-max_len:i]

        return lcs_str


###################################################
# 方法三： 中心扩散（时间花费顺序2）
#     注意奇偶，奇数中心是字符，偶数中心是一条线
###################################################
class Solution3:
    def longestPalindrome(self, s):
        if len(s) < 2 or s == s[::-1]:
            return s

        max_len, res = 1, s[0]
        for i in range(len(s)):
            res_odd = self.center_spread(s, len(s), i, i)
            res_even = self.center_spread(s, len(s), i, i+1)
            # 当前字符串
            cur_res = res_even if len(res_even) > len(res_odd) \
                else res_odd
            if max_len < len(cur_res):
                max_len = len(cur_res)
                res = cur_res
        return res


    def center_spread(self, s, size, left, right, ):
        while left >= 0 and right < size and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1: right]

###################################################
# 方法四： DP（时间花费顺序3）
#     dp[left][right]:(前开后闭)代表字符串
#     动态转换公式：
#         dp[left][right] = 1, s[left] == s[right] and ((right-left-1 <= 3) or dp[left+1][right-1])
#         dp[left][right] = 0, otherwise
###################################################
class Solution4(object):
    def longestPalindrome(self, s):
        if len(s) < 2 or s == s[::-1]:
            return s

        dp = [[0] * len(s) for _ in range(len(s))]
        max_len, res = 1, s[0]
        # 从末尾开始，往前查找回文字符串
        for r in range(len(s)):
            for l in range(r+1):
                if s[l] == s[r] and (r-l <= 2 or dp[l+1][r-1]):
                    dp[l][r] = 1
                if dp[l][r] and max_len < r-l+1:
                    res = s[l:r+1]
                    max_len = r - l + 1

        return res


if __name__ == "__main__":
    solu = Solution4()
    s = sys.stdin.readline()
    print(solu.longestPalindrome(s))
