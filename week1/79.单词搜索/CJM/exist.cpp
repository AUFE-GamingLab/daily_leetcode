class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if(word.length()==0)
            return true;
        if(board.length==0 || board[0].length==0)
            return false;
        visited = new boolean[board.length][board[0].length];
        char[]  words = word.toCharArray();
        for(int i = 0;i < board.length;i++)
        {
            for(int j = 0;j < board[0].length;j++)
            {
                if(board[i][j]==words[0])
                {
                    dfs(board,words,0,i,j);
                    if(exist)
                        return true;
                }
            }
        }
        return false;
    }
    void dfs(vector<vector<char>>& board,string words,int index,int x,int y )
    {
        if(index == words.length)
            return;

        if(x < 0 || y < 0 || x > board.length-1|| y > board[0].length-1|| visited[x][y] || board[x][y]!=words[index])
            return;
        dfs(board,words,index+1,x+1,y);
        dfs(board,words,index+1,x-1,y);
        dfs(board,words,index+1,x,y+1);
        dfs(board,words,index+1,x,y-1);
    }
};
