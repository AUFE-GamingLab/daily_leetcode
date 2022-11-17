class Solution {
    static int[] dx = new int[]{-1, 0, 1, 0};
    static int[] dy = new int[]{0, 1, 0, -1};
    Deque<int[]> deque = new ArrayDeque<>();
    void setAllVisit(int[][] grid,int x,int y){
        int n = grid.length;
        if(x < 0 || x > n - 1 || y < 0 || y > n - 1 || grid[x][y] != 1){
            return;
        }
        else {
            deque.offer(new int[]{x,y});
            grid[x][y] = -1;
        }
        for(int i = 0;i < 4;i++){
            setAllVisit(grid,x + dx[i],y + dy[i]);
        }
    }

    public int shortestBridge(int[][] grid) {
        int n = grid.length;
        for(int i = 0;i < n;i++){
            boolean st = false;
            for(int j = 0;j < n;j++){
                if(grid[i][j] == 1){
                    setAllVisit(grid,i,j);
                    st = true;
                    break;
                }
            }
            if(st){
                break;
            }
        }
        int res = 0;
        while(!deque.isEmpty()){
            int size = deque.size();
            for(int k = 0;k < size;k++){
                int[] pos = deque.poll();
                for(int i = 0;i < 4;i++){
                    int x = pos[0] + dx[i], y = pos[1] + dy[i];
                    if(x >= 0 && x < n && y >= 0 && y < n){
                        if(grid[x][y] == 0){
                            grid[x][y] = -1;
                            deque.offer(new int[]{x, y});
                        }
                        else if(grid[x][y] == 1){
                            return res;
                        }
                    }
                }
            }
            res++;
        }
        return 0;
    }
}
