class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int T = 0;
        int B = matrix.size();
        int L = 0;
        int R = matrix.size();

        while(T<=B) {
            int m_row = (T+B)/2;
            int m_col = (L+R)/2;

            if (target > matrix[m_row][m_col]) {
                T = m_row + 1;
                L = m_col + 1;
            } else if (target < matrix[m_row][m_col]){
                B = m_row - 1;
                R = m_col - 1;
            } else {
                return true;
            }
        }

        else false;
    }
};
