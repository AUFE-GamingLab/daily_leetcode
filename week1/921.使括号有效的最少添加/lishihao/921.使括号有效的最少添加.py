#
# @lc app=leetcode.cn id=921 lang=python3
#
# [921] 使括号有效的最少添加
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l = 0
        r = 0
        for i in range(len(s)):
            if s[i] == "(":
                l += 1
            else:
                if l>0:
                    l -= 1
                else:
                    r += 1
        return l+r
# @lc code=end

