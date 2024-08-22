class Solution {
public:
    map<int, bool> idxVisit;
    void dfs(int visit, vector<vector<int>>& rooms){
        idxVisit[visit] = true;
        if (rooms[visit].empty()) return;
        for(auto const& t: rooms[visit]){
            if (!idxVisit[t]) dfs(t, rooms);
        }
    }

    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        dfs(0,rooms);
        bool res = true;
        for(int i = 0;i<rooms.size();i++) res&=idxVisit[i];
        return res;
    }
};