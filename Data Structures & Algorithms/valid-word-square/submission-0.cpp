class Solution {
public:
    bool validWordSquare(vector<string>& words) {
        n = words.length();
        int row_length = 0;
        for(int i=0;i<n;i++){
            row_length = word[i].length();
            if(i != 0 && row_length != word[i].length()){
                return false;
            }
        }

        return true;
    }
};
