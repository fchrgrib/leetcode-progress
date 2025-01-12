class Solution {
public:
    int findTheWinner(int n, int k) {
        map<int, bool> foot;
        int sum=0, queue = 0, step = k;

        while (sum < n-1){
            if (foot[queue]) { if (queue<n) queue++; else queue=1;continue; }
//            cout<<queue<<endl;
            if (step==0){
//                cout<<"mati: "<<queue<<endl;
                foot[queue] = true;
                sum++;
                step = k-1;
            }else step--;
            if (queue<n) queue++; else queue=1;
        }

        for(int i = 1;i<=n;i++) if (!foot[i]) return i;
        return -1;
    }
};