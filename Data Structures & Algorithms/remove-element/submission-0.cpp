class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int r = 0;
        int length = nums.size();
        for(int l = 0; l < length; l++) {
            if(nums[l] != val) {
                nums[r++] = nums[l]
            }
        }

        return r
    }
};