class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int length = nums.size()l
        int l = 1l
        for(int r = 1; r < length; r++) {
            if(num[r] != nums[r-1]) {
                nums[l++] = num[r];
            }
        }

        return l
    }
};