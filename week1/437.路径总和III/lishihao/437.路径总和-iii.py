#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def rootSum(root,target):
            if root == None:
                return 0
            n = 0
            if target == root.val:
                n +=1
            n += rootSum(root.left,target-root.val)
            n += rootSum(root.right,target-root.val)
            return n
        #以自己为根节点
        res = rootSum(root,targetSum)
        #以左节点 右节点为根节点点
        if root == None:
            return 0
        res += self.pathSum(root.left,targetSum)
        res += self.pathSum(root.right,targetSum)
        return res


# @lc code=end

