class Solution {
public:
    // 预处理 记录每个字母最后出现的下标
    // 贪心策略：当前最小的结束下标 
    vector<int> partitionLabels(string s) {
        int len = s.size();
        int last[26];
        for(int i = 0; i < len; i++)
        {
            //! 如何记录字母-数字对？
            last[s[i] - 'a'] = i; // 0 代表 a，以此类推，统计最后一次出现的下标
        }

        vector<int> partition;
        int start = 0; // 片段开始
        int end   = 0; // 片段结束
        // 注意贪心策略，所以到 end 就结束就保证了是尽量最小的下标
        for(int i = 0; i < len; i++)
        {
            end = max(end, last[s[i] - 'a']);
            // 到头
            if(i == end)
            {
                partition.push_back(end - start + 1);
                start = end + 1;
            }
        }

        return partition;
    }
};