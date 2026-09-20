class Solution {
public:
    bool validWordSquare(vector<string>& words) {
        for(int wordNum = 0; wordNum < words.size(); ++wordNum) {
            for(int charPos = 0; charPos < words[wordNum].size(); ++charPos){
                if (charPos >= words.size() || 
                    wordNum >= words[charPos].size() || 
                    words[wordNums][charPos] != words[charPos][wordNums]) {
                    return false;
                }
            }
        }

        return true;
    }
};
