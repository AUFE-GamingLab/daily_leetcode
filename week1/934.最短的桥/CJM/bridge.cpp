class Solution {
public:
    vector<vector<int>>& signal = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int shortestBridge(vector<vector<int>>& grid) {
        int res = 0;
        bool[][] visited = new bool[grid.length][grid.length];
        Queue<int[]> isLand = new LinkedList<>();
        for (int i = 0; i < grid.length; i++) 
        {
            for (int j = 0; j < grid.length; j++) 
            {
                if (grid[i][j] == 1) {
                    dfs(i, j, visited, grid, isLand);
                    while (!isLand.isEmpty()) 
                    {
                        int size = isLand.size();
                        for (int k = 0; k < size; k++) 
                        {
                            int[] point = isLand.poll();
                            for (int m = 0; m < signal.length; m++) 
                            {
                                int x = point[0] + signal[m][0];
                                int y = point[1] + signal[m][1];
                                if (x >= 0 && x <= grid.length - 1 && y >= 0 && y <= grid.length - 1 && !visited[x][y]) 
                                {
                                    if (grid[x][y] == 0) 
                                    {
                                        visited[x][y] = true;
                                        isLand.add(new int[]{x, y});
                                    } 
                                    else if (grid[x][y] == 1)
                                    {
                                        return res;
                                    }
                                }
                            }
                        }
                        res++;
                    }
                }
            }
        }
        return res;
    }
    void dfs(int i, int j, bool[][] visited, int[][] grid, Queue<int[]> isLand) {
        if (i < 0 || i > grid.length - 1 || j < 0 || j > grid.length - 1 || grid[i][j] == 0 || visited[i][j]) {
            return;
        }
        visited[i][j] = true;
        isLand.add(new int[]{i, j});
        dfs(i - 1, j, visited, grid, isLand);
        dfs(i + 1, j, visited, grid, isLand);
        dfs(i, j - 1, visited, grid, isLand);
        dfs(i, j + 1, visited, grid, isLand);
    }
};
