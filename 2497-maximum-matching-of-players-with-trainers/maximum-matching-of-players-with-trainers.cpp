class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        int idxP = players.size()-1, idxT = trainers.size()-1, res = 0;
        sort(players.begin(), players.end());
        sort(trainers.begin(), trainers.end());

        while(idxP>=0 && idxT>=0){
            if(players[idxP]<=trainers[idxT]){
                res++;
                idxP--;idxT--;
            }else{
                idxP--;
            }
        }

        return res;
    }
};