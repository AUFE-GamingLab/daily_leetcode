class Solution {
public:
    void DfsGrid(vector<vector<char>>& grid, int r, int c){
        if(r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size() || grid[r][c] == '0'){
            return ;
        }

        grid[r][c] = '0';

        DfsGrid(grid, r - 1, c);
        DfsGrid(grid, r + 1, c);
        DfsGrid(grid, r, c - 1);
        DfsGrid(grid, r, c + 1);
    }

    int res = 0;
    int numIslands(vector<vector<char>>& grid) {
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[0].size(); j++){
                if(grid[i][j] == '1'){
                   DfsGrid(grid, i, j); 
                   res++;
                    
                }
            }
        }
        
        return res;
    }
};