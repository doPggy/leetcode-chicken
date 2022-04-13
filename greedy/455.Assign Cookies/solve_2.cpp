class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        // 贪心策略：用最少的满足
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int child = 0;
        int cookie = 0;
        while(child < g.size() && cookie < s.size())
        {
            // 能够满足小孩子
            if(s[cookie] >= g[child]) child++;
            cookie++; // 满不满足，都要选下一个饼干
        }
        return child; // 满足多少个孩子
    }
};