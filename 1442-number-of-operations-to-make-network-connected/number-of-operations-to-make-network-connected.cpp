class Solution {
public:
    set<int> node;
    map<int, long long> rank;
    map<int, int> edge;
    int res;

    int findParent(int n){
        int p = edge[n];
        while (p != edge[p]){
            p = edge[p];
        }
        return p;
    }

    void isRedundant(int n1, int n2){
        node.insert(n1);node.insert(n2);
        int p1 = findParent(n1), p2 = findParent(n2);

        if (p1 == p2) {
            res++;
            return;
        }

        if (rank[p1]>rank[p2]){
            edge[p2] = p1;
            rank[p1]+=rank[p2];
        }else{
            edge[p1] = p2;
            rank[p2]+=rank[p1];
        }
    }

    int makeConnected(int n, vector<vector<int>>& connections) {
        for(int i = 0;i<n;i++) { rank[i] = 1; edge[i] = i;}
        for(auto const c: connections){
            isRedundant(c[0],c[1]);
        }
        int c = 0;
        for(int i = 0;i<n;i++){
            if (findParent(i) == i) c++;
        }


        return (res>=(c-1))?(c-1):-1;
    }
};