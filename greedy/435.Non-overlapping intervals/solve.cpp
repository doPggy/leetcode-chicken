#include <algorithm>

using namespace std;

class Solution {
public:
    //! 保留区间，看头或者尾。贪心策略：优先保留结尾小，不相交区间
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if(intervals.empty()) return 0;

        int n = intervals.size();
        //! lamba 按照区间左端排序
        sort(intervals.begin(), intervals.end(), [](vector<int> &a, vector<int> &b) {
            return a[1] < b[1];
        });

        int total = 0;
        int prev  = intervals[0][1];
        //! 注意如何与前一个区间判断，如果中途有剔除一个区间，不需要真的剔除
        for(int i = 1; i < n; i++)
        {
            // 后一个和前一个区间相交了, 假剔除
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