class Solution {
public:
    set<vector<int>> res;
    void bc(vector<int>& candidates, int target, vector<int> path,int idx){
        if (target == 0){
            res.insert(path);
            return;
        }
        if (target<0){
            return;
        }

        for(int i=idx;i<candidates.size();i++){
            if (i > idx && candidates[i] == candidates[i - 1]) continue;


            if (candidates[i] > target) break;
            int temp = candidates[i];
            path.push_back(temp);
            bc(candidates, target-temp,path,i+1);
            path.pop_back();
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        int size = candidates.size();
        if(candidates[size-1] * size<target) return {};
        if((candidates[0] == candidates[size-1]) && candidates[size-1]* size >=target) {
            int step = target/candidates[0];
            if(step ==0 || step*candidates[0] != target) return {};
            return vector<vector<int>>(1, vector<int>(step, candidates[0]));
        }
        bc(candidates,target,{},0);
        return vector<vector<int>>(res.begin(), res.end());
    }
};