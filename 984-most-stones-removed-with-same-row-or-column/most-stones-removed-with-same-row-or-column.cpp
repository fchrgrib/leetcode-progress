class Solution {
public:
   map<pair<int, char>, pair<int,pair<int, char>>> unF;
    map<pair<int, char>, int> temp;
    void init(vector<vector<int>> stones){
        for(auto const& t: stones){
            unF[{t[0], 'x'}] = {0, {t[0], 'x'}};
            unF[{t[1], 'y'}] = {0, {t[1], 'y'}};
        }
    }
    void unionFind(int n1, int n2){
        auto par1 = getParent({n1, 'x'}), par2 = getParent({n2, 'y'});

        if(par1 == par2) return;

        if(unF[par1].first>unF[par2].first){
            unF[par2].second = par1;
            unF[par1].first++;
        }else{
            unF[par1].second = par2;
            unF[par2].first++;
        }
    }
    pair<int, char> getParent(pair<int, char> n){
        auto par = unF[n].second;
        while(n!=par) { n = par; par = unF[par].second; }
        return n;
    }
    int removeStones(vector<vector<int>>& stones) {
        int res = 0;
        init(stones);
        for(auto const& t: stones){
            unionFind(t[0], t[1]);
        }
        for(auto const& t: stones){
            pair<int, char> x = {t[0], 'x'},
                    y = {t[1], 'y'},
                    parX1 = getParent(x),
                    parY1 = getParent(y);
            temp[parY1]++;temp[parX1]++;
        }
        for(auto const& t: temp){
            int tmp = t.second/2-1;
            if (tmp!=0) res+=(tmp);
        }
        return res;
    }
};