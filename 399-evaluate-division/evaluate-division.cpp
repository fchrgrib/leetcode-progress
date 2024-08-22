class Solution {
public:
map<string, pair<string, double>> parent;
    map<string, int> rank;

    string findParent(string n){
        if (parent[n].first != n) {
            string originalParent = parent[n].first;
            parent[n].first = findParent(parent[n].first);
            parent[n].second *= parent[originalParent].second;
        }
        return parent[n].first;
    }

    void unionFind(string n1, string n2, double val){
        string p1 = findParent(n1),p2 = findParent(n2);

        if (p1 == p2) return;

        if (rank[p1] >= rank[p2]) {
            parent[p2] = {p1, (parent[n1].second * val) / parent[n2].second};
            if (rank[p1] == rank[p2]) rank[p1]++;
        } else {
            parent[p1] = {p2, parent[n2].second / (val * parent[n1].second)};
        }
    }

    vector<double> calcEquation(
            vector<vector<string>>& equations,
            vector<double>& values,
            vector<vector<string>>& queries
    ) {
        vector<double> res;
        for (int i = 0; i < equations.size(); i++) {
            string a = equations[i][0], b = equations[i][1];
            if (!parent.count(a)) parent[a] = {a, 1.0};
            if (!parent.count(b)) parent[b] = {b, 1.0};
            unionFind(a, b, values[i]);
        }

        for(auto const& q: queries){
            if (parent.count(q[0]) && parent.count(q[1])){
                string p1 = findParent(q[0]);
                string p2 = findParent(q[1]);
                if (p1 != p2) res.push_back(-1.0);
                else res.push_back(1/(parent[q[0]].second / parent[q[1]].second));
            }else res.push_back(-1);
        }

        return res;
    }
};