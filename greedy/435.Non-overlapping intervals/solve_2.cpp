class Solution {
public:
    // 区间问题
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {

        if(intervals.empty()) return 0;

        int n = intervals.size();
        // 选择的区间结尾越小，余留给其它区间的空间
        // 就越大，就越能保留更多的区间。因此，我们采取的贪心策略为，优先保留结尾小且不相交的区间
        sort(intervals.begin(), intervals.end(), [](vector<int> &a, vector<int> &b){
            //! 按照区间右端排序！
            return a[1] < b[1];
        });
        int prev = intervals[0][1];
        int total = 0;
        for(int i = 1; i < n; i++)
        {
            if(intervals[i][0] < prev)
            {
                total++;
            }
            else
            {
                prev = intervals[i][1];
            }
        }

        return total;
    }
};