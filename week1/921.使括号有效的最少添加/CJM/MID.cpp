class Solution {
public:
    int minAddToMakeValid(string s) {
        stack<char> S;
        for (int i = 0; i < s.length(); i++) {
            if (S.empty()) {
                S.push(s[i]);
                continue;
            }
            if (S.top() == '(' && s[i] == ')') {
                S.pop();
            }else {
                S.push(s[i]);
            }
        }
        return (int)S.size();
    }
};
