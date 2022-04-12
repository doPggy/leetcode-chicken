#include <algorithm>

using namespace std;

class Solution {
public:
    // g 是 小孩饥饿度，s 饼干量
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        // 指针
        int child = 0;
        int cookie = 0;
        int child_size  = g.size();
        int cookie_size = s.size();
        while(child < child_size && cookie < cookie_size)
        {
            if(g[child] <= s[cookie]) child++;
            cookie++;
        }
        return child;
    }
};