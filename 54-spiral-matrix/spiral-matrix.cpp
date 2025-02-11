class Solution {
public:
    void bc(int start, int row, int col,vector<vector<int>>& matrix, vector<int>& res){
        if(start>= row || start>=col) return;
        for(int i = start;i<col;i++) res.push_back(matrix[start][i]);
        for(int i = start+1;i<row;i++) res.push_back(matrix[i][col-1]);
        if (start < row - 1) for (int i = col - 2; i >= start; i--) res.push_back(matrix[row - 1][i]);
        if (start < col - 1) for (int i = row - 2; i > start; i--) res.push_back(matrix[i][start]);
        bc(start+1, row-1, col-1, matrix, res);
    }
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        bc(0, matrix.size(), matrix[0].size(), matrix, res);
        return res;
    }
};