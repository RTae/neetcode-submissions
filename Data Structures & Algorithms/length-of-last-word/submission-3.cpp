class Solution {
public:
    int lengthOfLastWord(string s) {
        // The idea is we need to step backward and when meet a next space it mean it's a last word
        n = s.length();
        i = n-1;
        res = 0;
        // Remove space at the end
        while(s[i] == ' ') i--;
        // Found last word and stop when meet another space
        while(i>=0 && s[i] != ' '){
            // step down
            i--;
            // count word
            res++;
        }

        return res;
    }
};