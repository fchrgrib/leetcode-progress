class Solution {
public:
    void dfs(int l, int r, vector<vector<char>>& grid, vector<vector<bool>>& visit, int col, int row){
        if(visit[l][r]) return;
        visit[l][r] = true;

        if(l-1>=0 && grid[l-1][r] == '1') dfs(l-1, r, grid, visit, col, row);
        if(l+1< row && grid[l+1][r] == '1') dfs(l+1, r, grid, visit, col, row);
        if(r-1>=0 && grid[l][r-1] == '1') dfs(l, r-1, grid, visit, col, row);
        if(r+1<col && grid[l][r+1] == '1') dfs(l, r+1, grid, visit, col, row);
    }
    int numIslands(vector<vector<char>>& grid) {
        vector<vector<bool>> visit(grid.size(), vector<bool>(grid[0].size(), false));

        int row = grid.size(), col = grid[0].size(), sum=0;

        for(int i = 0;i<row;i++){
            for(int j = 0; j<col;j++){
                if(grid[i][j] == '0' || visit[i][j]) continue;
                sum++;
                dfs(i, j, grid, visit, col, row);
            }
        }

        return sum;
    }
};