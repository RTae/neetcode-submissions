class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int length = nums.size();
        int l = 1;

        for(r=1; r < lenght; r++) {
            if(nums[r] != nums[r-1]){
                nums[l++] = nums[r];
            }
        }

        return l;
    }
};

