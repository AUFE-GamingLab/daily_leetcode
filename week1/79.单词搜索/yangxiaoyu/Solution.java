class Solution {
    private boolean dfs(char[][]board,String word,int i,int j,int index){
    //边界判断，当前字符是否相等以及是否遍历到目标单词的最后一位
if(i>=board.length||i<0||j>=board[0].length||j<0||board[i][j]!=word.charAt(index) )          return false;
        if(index == word.length()-1) 
          return true;
        char tmp = board[i][j];
        board[i][j]='#';
        boolean res = dfs(board,word,i+1,j,index+1)||dfs(board,word,i-1,j,index+1)||dfs(board,word,i,j+1,index+1)||dfs(board,word,i,j-1,index+1);
        board[i][j] = tmp;
        return res;

    }
    public boolean exist(char[][] board, String word) {
        for(int i=0;i<board.length;i++){
            for(int j=0;j<board[0].length;j++){
               //枚举，从每个点向四周搜索是否能构成目标单词
                if(dfs(board,word,i,j,0)==true) return true;
            }
        }
        return false;
    }
}