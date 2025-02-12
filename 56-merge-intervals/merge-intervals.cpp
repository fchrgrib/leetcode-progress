class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        int idx = 0;
        vector<vector<int>> res;

        for(int i = 0;i<intervals.size();i++){
            if(i == 0){
                res.push_back({intervals[i][0],intervals[i][1]});
                continue;
            }

            if(res[idx][1]>=intervals[i][0]){
                res[idx][1] = max(res[idx][1], intervals[i][1]);
            }else{    
                res.push_back({intervals[i][0],intervals[i][1]});                                                                                                                                                                                                                                                                                                 
                idx++;
            }    
        }


        // if(res[res.size()-1][1]<=start) res.push_back({start, end});
        // res.push_back({start, end});

        return res;
    }
};