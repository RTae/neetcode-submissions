class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int T = 0;
        int B = matrix.size() - 1;

        while(T<=B) {
            int m_row = (T+B)/2;

            if (target > matrix[m_row].back()) {
                T = m_row + 1;
            } else if (target < matrix[m_row][0]){
                B = m_row - 1;
            } else {
                break;
            }
        }
        if (!(T <= B)) return false;

        int L = 0;
        int R = matrix[0].size() - 1;
        int row = (T + B)/2;

        while(L<=R) {
            int m_col = (L+R)/2;
            
            if (target > matrix[row][m_col]) {
                L = m_col + 1;
            } else if (target < matrix[row][m_col]){
                R = m_col - 1;
            } else {
                return true;
            }
        }

        return false;
    }
};
