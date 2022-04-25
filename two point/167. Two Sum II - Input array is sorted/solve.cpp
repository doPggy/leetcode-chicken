class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int len   = numbers.size();
        int end   = len - 1;
        int start = 0;
        int sum   = 0;
        // vector<int> ans;
        // [3 6 3 5 3]
        // 排好序的可以头尾双指针，类似快排中分区思想
        while(start < end)
        {
            sum = numbers[start] + numbers[end];
            if(sum > target) end--;
            else if(sum < target) start++;
            else break;
            // while(numbers[start] + numbers[end] > target) --end;
            // while(numbers[start] + numbers[end] < target) ++start;
        }
        return vector<int>{start + 1, end + 1};
    }
};