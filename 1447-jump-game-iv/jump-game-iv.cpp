class Solution {
public:
    int minJumps(vector<int>& arr) {
        unordered_map<int, vector<int>> memoEl;
        map<int , bool> isFoot; queue<pair<int, int>> q;
        int size = arr.size(), sum = 0;
        if(arr[size - 1] == arr[0] && size>1) return 1;
        
        for(int i = 0;i<size;i++) memoEl[arr[i]].push_back(i);
        q.push({0, 0});
        isFoot[0] = true;

        // for(auto t: memo[0]) cout<<t<<endl;

        while(!q.empty()){
            int idx = q.front().first, step = q.front().second;
            q.pop();

            if(idx == size-1) return step;
            cout<<idx<<endl;

            if(idx-1>=0 && !isFoot[idx-1]){
                isFoot[idx-1] = true;
                q.push({idx-1, step+1});
            }
            if(idx+1<size && !isFoot[idx+1]){
                isFoot[idx+1] = true;
                q.push({idx+1, step+1});
            }

            for(auto t: memoEl[arr[idx]]){
                if(!isFoot[t]){
                    isFoot[t] = true;
                    q.push({t, step+1});
                }
            }
            
            memoEl[arr[idx]].clear();
        }
        return 0;
    }
};