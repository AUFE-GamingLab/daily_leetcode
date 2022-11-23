class Solution {
public:
    vector<string> letterCasePermutation(string s) {
   queue<string> que; 
        que.push(s);
        for(int i = 0; i < s.size(); i++)
        {
            if(!(s[i] >= '0' && s[i] <= '9'))
            {
                int size = que.size();
                while(size > 0)
                {
                    string cur = que.front();
                    que.push(cur);
                    cur[i] = cur[i] <= 90 ? (cur[i] + 32) : (cur[i] - 32);
                    que.push(cur);
                    que.pop();
                    size--;
                }
            }
        }
        vector<string> ans;
        while(!que.empty())
        {
            string &cur = que.front();
            ans.push_back(cur);
            que.pop();
        }
        return ans;
    }
};
