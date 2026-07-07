class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int leng = nums.size();
        vector<int> res(2 * leng);
        for (int i = 0; i < leng; i++) {
            res[i] = res[i+leng] = nums[i];
        }
        return res;
    }
};