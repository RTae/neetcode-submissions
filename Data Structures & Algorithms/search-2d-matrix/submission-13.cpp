class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n_row = matrix.size()-1;
        int n_col = matrix[0].size()-1;
        int T = 0;
        int B = n_row;

        while(T<=B) {
            int m_row = (T+B)/2;

            if(target > matrix[m_row].back()) {
                T = m_row + 1;
            } else if (target < matrix[m_row][0]) {
                B = m_row - 1;
            } else {
                break;
            }
        }

        if (!(T<=B)) return false;

        int L = 0;
        int R = n_col;
        int ROW = (T+B)/2;

        while(L <= R){
            int m_col = (L+R)/2;
            if(target > matrix[ROW][m_col]) {
                L = m_col + 1;
            } else if (target < matrix[ROW][m_col]) {
                R = m_col - 1;
            } else {
                return true;
            }
        }

        return false;
    }
};
