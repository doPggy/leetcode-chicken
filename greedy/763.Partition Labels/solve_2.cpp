class Solution {
public:
    vector<int> partitionLabels(string s) {
        int s = s.size();
        int last[26];
        // 预处理 记录最后一次出现，尽量包括短的范围
        for(int i = 0; i < s; i++)
        {
            last[s[i] - 'a'] = i;
        }

        vector<int> part;
        int start = 0;
        int end = 0;
        for(int i = 0; i < s; i++)
        {
            end = max(end, last[s[i] - 'a']);
            if(i == end)
            {
                part.push_back(end - start + 1);
                start = end + 1;
            }
        }
        return part;
    }
};