class Solution {
public:
    map<int, int> garden;
map<int, vector<int>> child;
vector<int> res;

void dfs(int g, int n, const vector<int>& t) {
    if (n == res.size()) return;

    vector<int> p = {1, 2, 3, 4};
    int next = 0;

    for (auto tmp : t) {
        if (garden[tmp] != 0) {
            p.erase(remove(p.begin(), p.end(), garden[tmp]), p.end());
        } else {
            next = tmp;
        }
    }

    garden[g] = p[0];
    if (next) dfs(next, n, child[next]);
}

void init(const vector<vector<int>>& paths) {
    for (const auto& p : paths) {
        child[p[0]].push_back(p[1]);
        child[p[1]].push_back(p[0]);
    }
}

vector<int> gardenNoAdj(int n, const vector<vector<int>>& paths) {
    init(paths);
    for (const auto& t : child) {
        if (!garden[t.first]) dfs(t.first, n, child[t.first]);
    }
    res.reserve(n);
    for (int i = 1; i <= n; i++) {
        res.push_back(garden[i] ? garden[i] : 1);
    }
    return res;
}
};