#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(temp,s,i):
            if s > target or i == len(candidates):
                return
            elif s == target:
                res.append(temp)
                return
            #取
            backtrack(temp+[candidates[i]],s+candidates[i],i)
            #不取
            backtrack(temp,s,i+1)
        backtrack([],0,0)

        return res
# @lc code=end

