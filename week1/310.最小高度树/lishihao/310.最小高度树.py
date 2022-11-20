#
# @lc app=leetcode.cn id=310 lang=python3
#
# [310] 最小高度树
#

# @lc code=start
class Solution:
    # def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    #     #bfs
    #     l = [[] for i in range(n)]
    #     for i in edges:
    #         l[i[0]].append(i[1])
    #         l[i[1]].append(i[0])
    #     min_d = 100000
    #     res = []
    #     for i in range(n):
    #         temp = [i] #储存每一个队列
    #         r = [False for i in range(n)]
    #         r[i] = True
    #         num = 1 # 不是len(num)
    #         d = 0
    #         while temp != []:#直到整个队列为空
    #             t = temp.pop(0) #返回当前被取出的值
    #             num = num - 1
    #             for j in l[t] : #访问子节点 保证该节点之前一定没有被访问过
    #                 if r[j] == False:
    #                     temp.append(j)
    #                     r[j] = True
    #             if num == 0:
    #                 num = len(temp)
    #                 d += 1
    #         if d < min_d :
    #             min_d = d
    #             res = [i]
    #         elif d == min_d:
    #             res.append(i)
    #     return res
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0] * n

        def bfs(start: int):
            vis = [False] * n
            vis[start] = True
            q = deque([start])
            while q:
                x = q.popleft()
                for y in g[x]:
                    if not vis[y]:
                        vis[y] = True
                        parents[y] = x
                        q.append(y)
            return x
        x = bfs(0)  # 找到与节点 0 最远的节点 x
        y = bfs(x)  # 找到与节点 x 最远的节点 y

        path = []
        parents[x] = -1
        while y != -1:
            path.append(y)
            y = parents[y]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]
# @lc code=end

