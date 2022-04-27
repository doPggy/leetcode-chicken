class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int pos = m-- + n-- - 1;
        // 指向有数据的末尾
        while(m >= 0 && n >= 0)
        {
            nums1[pos--] = nums1[m] > nums2[n] ? nums1[m--] : nums2[n--];
        }

        // [3, 4, 0, 0] [1, 2]
        while(n >= 0)
        {
            nums1[pos--] = nums2[n--];
        }
    }
};