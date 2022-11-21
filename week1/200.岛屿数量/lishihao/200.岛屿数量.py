#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x = len(grid)+2
        y = len(grid[0])+2
        num = 0
        def dfs(i,j):
            if temp[i][j] == "0" or temp[i][j] == "2":
                return
            dfs(i-1,j)
            dfs(i,j-1)
            temp[i][j] = "0"
            dfs(i,j+1)
            dfs(i+1,j)


        #dfs
        temp = [["2" for _ in range(y)] for _ in range(x)]
        for i in range(1,x-1):
            for j in range(1,y-1):
                temp[i][j] = grid[i-1][j-1]
        for i in range(1,x-1):
            for j in range(1,y-1):
                if temp[i][j] == "1":
                    num = num+1
                    dfs(i,j)
        
        return num
                    
# @lc code=end

