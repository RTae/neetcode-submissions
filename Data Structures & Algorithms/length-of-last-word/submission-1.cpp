class Solution {
public:
    int lengthOfLastWord(string s) {
        int n = s.length();
        int i = n-1;
        int length = 0;
        // Remove space from last word
        // we need to step backward
        while(s[i] == ' ') i--;
        // it mean we found last word
        while(s[i] != ' ' && i>=0){
            // Keep track length while count last word
            i--;
            length++;
        }
        return length;
    }
};