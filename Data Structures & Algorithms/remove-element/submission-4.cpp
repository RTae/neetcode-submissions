class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int l = 0;
        int length = nums.size();
        for(int r = 0; r < length; r++) {
            if(nums[r] != val) {
                nums[l++] = nums[r];
            }
        }

        return l;
    }
};