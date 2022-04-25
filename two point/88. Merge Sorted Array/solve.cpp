class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // 排好序的数组，可以考虑从后往前，找较大的，而不一定要从前往后遍历。
        // int i = m - 1;
        // int j = n - 1;
        int pos = m-- + n-- - 1; //! 这里要理解，num1 会被拓展, 但是遍历是从 最后一个数据往前遍历！
        // [4, 6, 0, 0], [3, 5] //! 不是从 num1 最后一个和 num2 最后一个，这样永远会 nums2 复制在尾部

        //! 所以 nums2 没有复制完就要接着复制

        while(m >= 0 && n >= 0)
        {
            nums1[pos--] = nums1[m] >= nums2[n] ? nums1[m--] : nums2[n--];
        }

        while(n >= 0)
        {
            nums1[pos--] = nums2[n--];
        }

    }
};