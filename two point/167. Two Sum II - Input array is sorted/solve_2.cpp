class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0;
        int j = numbers.size() - 1;
        int sum = 0;
        // 两边向中间遍历
        while(i < j)
        {
            sum = numbers[i] + numbers[j];
            if(target == sum) break;
            else if(target < sum) i++;
            else if(target < sum) j--;
        }
        return vector<int>{i + 1, j + 1};
    }
};