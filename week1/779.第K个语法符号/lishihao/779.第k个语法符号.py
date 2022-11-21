#
# @lc app=leetcode.cn id=779 lang=python3
#
# [779] 第K个语法符号
#

# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # t1 = "0"#暂时储存数据
        # t2 = "0"#储存最终的数字
        # for i in range(n):
        #     while t1 != "":
        #         t = t1[0]
        #         t1 = t1[1:]
        #         if t == "0":
        #             t2 +="01"
        #         else:
        #             t2 +="10"
        #     t1 = t2
        #     t2 = ""
        # return int(t1[k-1])
        if n == 1:
            return 0
        return (k & 1) ^ 1 ^ self.kthGrammar(n - 1, (k + 1) // 2)

             
# @lc code=end

