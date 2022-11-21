#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def add(temp,i):
            if i == len(s):
                res.append(temp)
                return
            if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >='A' and s[i] <= 'Z'):
                add(temp+str.upper(s[i]),i+1)
                add(temp+str.lower(s[i]),i+1)
            else:
                add(temp+s[i],i+1)
            return 
        add("",0)
        return res
# @lc code=end

