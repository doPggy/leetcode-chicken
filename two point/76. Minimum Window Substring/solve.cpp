class Solution {
public:
    string minWindow(string s, string t) {
        // 使用滑动窗口
        vector<bool> flag(128, false); // 是否在 T 中
        vector<int> chars(128, 0); // 当前窗口内， T 中字符缺少的数量, 负值代表虽然是 T 中字符，但是已经重复
        // 统计 T 的信息
        //! for(int i = 0; i < s.size(); i++) 怎么统计 S 了！！！！
        for(int i = 0; i < t.size(); i++)
        {
            flag[t[i]] = true;
            ++chars[t[i]];
        }

        // 滑动
        int cnt = 0; // 当前满足 T 的字符个数
        int l = 0, r = 0;
        int min_l = 0;
        int min_size = s.size() + 1;
        for(r = 0; r < s.size(); r++)
        {
            if(!flag[s[r]]) continue;
            // 若是 T 中的字符之一

            // 新的字符纳入
            if(--chars[s[r]] >= 0)
                ++cnt;

            // 若 S[l] 一直是指定字符外的字符，就一直缩小窗口           
            while(cnt == t.size())
            {
                // 记录最小窗口
                if(r - l + 1 < min_size)
                {
                    min_l    = l;
                    min_size = r - l + 1;
                }

                // 如果窗口左端是 T 中指定字符，并且非重复项
                //! ++chars 要体会
                if(flag[s[l]] && ++chars[s[l]] > 0)
                {
                    --cnt;
                }
                ++l;
            }
        }

        return min_size > s.size() ? "" : s.substr(min_l, min_size);
 
    }
};