class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dir = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(i,j):
            queue = collections.deque()
            queue.append((i,j,0))
            while queue:
                x,y,time = queue.popleft()
                for dx,dy in dir:
                    nx,ny = x + dx, y + dy
                    if nx >= 0 and nx < m and ny >= 0 and ny < n and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        if grid[nx][ny] == 1:
                            if time >= 1:
                                return time
                            else:
                                queue.appendleft((nx,ny,0))
                        else:
                            queue.append((nx,ny,time+1))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited[i][j] = True
                    return dfs(i,j)